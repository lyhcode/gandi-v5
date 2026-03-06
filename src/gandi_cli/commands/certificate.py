"""Certificate management commands."""

from typing import Annotated, Optional

import typer

from gandi_cli.client import GandiClient, GandiAPIError
from gandi_cli.output import output

cert_app = typer.Typer(help="Certificate management", no_args_is_help=True)


def _get_client() -> GandiClient:
    from gandi_cli.main import state

    if not state.token:
        typer.echo(
            "Error: No API token. Run 'gandi auth login' or set GANDI_PAT.",
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
