"""Certificate management commands."""

from pathlib import Path
from typing import Annotated, Optional

import typer

from gandi_cli.client import GandiClient, GandiAPIError
from gandi_cli.output import output

cert_app = typer.Typer(help="Certificate management", no_args_is_help=True)


def _get_client() -> GandiClient:
    from gandi_cli.main import state

    if not state.token:
        typer.echo(
            "Error: No API token. Run 'gandi-v5 auth login' or set GANDI_PAT.",
            err=True,
        )
        raise typer.Exit(1)
    return GandiClient(token=state.token, sharing_id=state.sharing_id, sandbox=state.sandbox)


@cert_app.command("list")
def cert_list(
    cn: Annotated[
        Optional[str], typer.Option(help="Filter by Common Name")
    ] = None,
    status: Annotated[
        Optional[str],
        typer.Option(help="Filter by status (valid, expired, pending, revoked)"),
    ] = None,
    per_page: Annotated[int, typer.Option(help="Items per page")] = 25,
    page: Annotated[int, typer.Option(help="Page number")] = 1,
):
    """List SSL certificates."""
    client = _get_client()
    params: dict = {"page": page, "per_page": per_page}
    if cn:
        params["cn"] = cn
    if status:
        params["status"] = status
    try:
        data = client.get("/certificate/issued-certs", params=params)
        from gandi_cli.main import state

        columns = [
            ("id", "ID"),
            ("cn", "Common Name"),
            ("status", "Status"),
            ("dates.ends_at", "Expires"),
            ("package", "Package"),
        ]
        # Flatten nested fields for table display
        for item in data:
            dates = item.get("dates", {})
            item["dates.ends_at"] = (dates.get("ends_at") or "")[:10]
            item["package"] = (
                item.get("package", {}).get("name", "")
                if isinstance(item.get("package"), dict)
                else str(item.get("package", ""))
            )
        output(data, fmt=state.output_format, columns=columns, title="Certificates")
    except GandiAPIError as e:
        typer.echo(f"Error: {e}", err=True)
        raise typer.Exit(1)


@cert_app.command("info")
def cert_info(
    cert_id: Annotated[str, typer.Argument(help="Certificate ID")],
):
    """Show certificate details."""
    client = _get_client()
    try:
        data = client.get(f"/certificate/issued-certs/{cert_id}")
        from gandi_cli.main import state

        dates = data.get("dates", {})
        fields = [
            ("id", "ID"),
            ("cn", "Common Name"),
            ("status", "Status"),
            ("altnames", "Alt Names"),
            ("package_name", "Package"),
            ("starts_at", "Valid From"),
            ("ends_at", "Valid Until"),
        ]
        data["altnames"] = ", ".join(data.get("altnames", []))
        data["package_name"] = (
            data.get("package", {}).get("name", "")
            if isinstance(data.get("package"), dict)
            else str(data.get("package", ""))
        )
        data["starts_at"] = (dates.get("starts_at") or "")[:10]
        data["ends_at"] = (dates.get("ends_at") or "")[:10]
        output(data, fmt=state.output_format, detail_fields=fields)
    except GandiAPIError as e:
        typer.echo(f"Error: {e}", err=True)
        raise typer.Exit(1)


@cert_app.command("reissue")
def cert_reissue(
    cert_id: Annotated[str, typer.Argument(help="Certificate ID")],
    csr: Annotated[
        Path,
        typer.Option("--csr", help="Path to PEM-encoded CSR file"),
    ],
    dcv_method: Annotated[
        Optional[str],
        typer.Option(
            "--dcv-method",
            help="Domain validation method: email, dns, file, http, https",
        ),
    ] = None,
    duration: Annotated[
        Optional[int],
        typer.Option("--duration", help="Certificate duration in years"),
    ] = None,
    dry_run: Annotated[
        bool,
        typer.Option("--dry-run", help="Validate parameters without performing the operation"),
    ] = False,
):
    """Reissue (renew) a certificate.

    Submits a new CSR to reissue an existing certificate. Requires a
    PEM-encoded CSR file. After reissue, use 'cert dcv-info' to retrieve
    domain validation parameters and 'cert download' to fetch the issued
    certificate.
    """
    client = _get_client()
    try:
        csr_text = csr.read_text()
    except FileNotFoundError:
        typer.echo(f"Error: CSR file not found: {csr}", err=True)
        raise typer.Exit(1)
    except OSError as e:
        typer.echo(f"Error reading CSR file: {e}", err=True)
        raise typer.Exit(1)

    body: dict = {"csr": csr_text}
    if dcv_method:
        body["dcv_method"] = dcv_method
    if duration is not None:
        body["duration"] = duration

    headers = {}
    if dry_run:
        headers["Dry-Run"] = "1"

    try:
        data = client.post(
            f"/certificate/issued-certs/{cert_id}",
            json=body,
            headers=headers,
        )
        from gandi_cli.main import state

        if dry_run:
            typer.echo("Dry run: parameters are valid.")
        else:
            typer.echo(f"Certificate {cert_id} reissue submitted.")
        if isinstance(data, dict) and data:
            output(data, fmt=state.output_format, detail_fields=[
                ("message", "Message"),
            ])
    except GandiAPIError as e:
        typer.echo(f"Error: {e}", err=True)
        raise typer.Exit(1)


@cert_app.command("dcv-info")
def cert_dcv_info(
    cert_id: Annotated[str, typer.Argument(help="Certificate ID")],
    csr: Annotated[
        Optional[Path],
        typer.Option("--csr", help="Path to PEM-encoded CSR file"),
    ] = None,
    dcv_method: Annotated[
        Optional[str],
        typer.Option(
            "--dcv-method",
            help="DCV method to get params for: email, dns, file, http, https",
        ),
    ] = None,
    package: Annotated[
        Optional[str],
        typer.Option("--package", help="Certificate package name"),
    ] = None,
):
    """Get Domain Control Validation (DCV) parameters for a certificate.

    Returns the DNS record or file content needed to complete domain
    validation. Useful after 'cert reissue' to determine what validation
    step is required.
    """
    client = _get_client()

    body: dict = {}
    if csr:
        try:
            body["csr"] = csr.read_text()
        except FileNotFoundError:
            typer.echo(f"Error: CSR file not found: {csr}", err=True)
            raise typer.Exit(1)
        except OSError as e:
            typer.echo(f"Error reading CSR file: {e}", err=True)
            raise typer.Exit(1)
    if dcv_method:
        body["dcv_method"] = dcv_method
    if package:
        body["package"] = package

    try:
        data = client.post(
            f"/certificate/issued-certs/{cert_id}/dcv_params",
            json=body,
        )
        from gandi_cli.main import state

        output(data, fmt=state.output_format)
    except GandiAPIError as e:
        typer.echo(f"Error: {e}", err=True)
        raise typer.Exit(1)


@cert_app.command("download")
def cert_download(
    cert_id: Annotated[str, typer.Argument(help="Certificate ID")],
    output_file: Annotated[
        Optional[Path],
        typer.Option("--output", "-o", help="Write certificate to file instead of stdout"),
    ] = None,
):
    """Download the issued certificate PEM.

    Retrieves the certificate data for a given certificate ID. By default
    prints to stdout; use --output to write to a file.
    """
    client = _get_client()
    try:
        data = client.get(
            f"/certificate/issued-certs/{cert_id}/crt",
            headers={"Accept": "text/plain"},
        )
        if output_file:
            output_file.write_text(data if isinstance(data, str) else str(data))
            typer.echo(f"Certificate written to {output_file}")
        else:
            typer.echo(data if isinstance(data, str) else str(data), nl=False)
    except GandiAPIError as e:
        typer.echo(f"Error: {e}", err=True)
        raise typer.Exit(1)
