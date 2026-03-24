"""Certificate management commands."""

import subprocess
from pathlib import Path
from typing import Annotated, Optional

import typer

from gandi_cli.client import GandiClient, GandiAPIError
from gandi_cli.output import output, print_json_output

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


@cert_app.command("csr")
def cert_csr(
    domain: Annotated[str, typer.Argument(help="Domain name (used as filename base and CN)")],
    output_dir: Annotated[
        Path,
        typer.Option("--output-dir", "-d", help="Directory for key and CSR files"),
    ] = Path("."),
    subject: Annotated[
        Optional[str],
        typer.Option("--subject", "-s", help="Full subject string (overrides default /CN=domain)"),
    ] = None,
):
    """Generate a private key and CSR for a domain.

    Runs openssl to create a 2048-bit RSA key and a SHA-256 CSR.
    Files are written to OUTPUT_DIR as DOMAIN.key and DOMAIN.csr.

    Will refuse to overwrite an existing .key file to prevent
    accidental private key loss. Remove or rename it first if you
    need to regenerate.
    """
    output_dir.mkdir(parents=True, exist_ok=True)
    key_file = output_dir / f"{domain}.key"
    csr_file = output_dir / f"{domain}.csr"

    if key_file.exists():
        typer.echo(
            f"Error: Key file already exists: {key_file}\n"
            f"Remove or rename it before generating a new key.",
            err=True,
        )
        raise typer.Exit(1)

    subj = subject or f"/CN={domain}"
    cmd = [
        "openssl", "req", "-new", "-sha256",
        "-newkey", "rsa:2048", "-nodes",
        "-keyout", str(key_file),
        "-out", str(csr_file),
        "-subj", subj,
    ]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
    except FileNotFoundError:
        typer.echo("Error: openssl not found. Install OpenSSL and try again.", err=True)
        raise typer.Exit(1)

    if result.returncode != 0:
        typer.echo(f"Error: openssl failed:\n{result.stderr}", err=True)
        raise typer.Exit(1)

    from gandi_cli.main import state

    if state.output_format == "json":
        print_json_output({"key": str(key_file), "csr": str(csr_file)})
    else:
        typer.echo(f"Key:  {key_file}")
        typer.echo(f"CSR:  {csr_file}")


@cert_app.command("issue")
def cert_issue(
    csr: Annotated[
        Path,
        typer.Option("--csr", help="Path to PEM-encoded CSR file"),
    ],
    package: Annotated[
        str,
        typer.Option("--package", help="Certificate package name (e.g. cert_std_1_10_0_digicert)"),
    ],
    dcv_method: Annotated[
        Optional[str],
        typer.Option(
            "--dcv-method",
            help="Domain validation method: email, dns, file, http, https",
        ),
    ] = None,
    altnames: Annotated[
        Optional[str],
        typer.Option("--altnames", help="Comma-separated Subject Alternative Names"),
    ] = None,
    dry_run: Annotated[
        bool,
        typer.Option("--dry-run", help="Validate parameters without placing the order"),
    ] = False,
):
    """Purchase and issue a new certificate.

    Submits a CSR to order a new certificate with the specified package.
    Use 'cert csr' to generate the CSR first, and 'gandi cert packages'
    or the Gandi docs to find available package names.

    After issuing, use 'cert dcv-info' to get domain validation
    parameters and 'cert download' to retrieve the signed certificate.
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

    body: dict = {"csr": csr_text, "package": package}
    if dcv_method:
        body["dcv_method"] = dcv_method
    if altnames:
        body["altnames"] = [s.strip() for s in altnames.split(",")]

    headers = {}
    if dry_run:
        headers["Dry-Run"] = "1"

    try:
        data = client.post(
            "/certificate/issued-certs",
            json=body,
            headers=headers,
        )
        from gandi_cli.main import state

        if state.output_format == "json":
            print_json_output(data if data else {"dry_run": dry_run})
        else:
            if dry_run:
                typer.echo("Dry run: parameters are valid.")
            else:
                typer.echo("Certificate order submitted.")
            if isinstance(data, dict) and data:
                fields = [
                    ("id", "Certificate ID"),
                    ("message", "Message"),
                ]
                output(data, fmt=state.output_format, detail_fields=fields)
    except GandiAPIError as e:
        typer.echo(f"Error: {e}", err=True)
        raise typer.Exit(1)


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

        if state.output_format == "json":
            print_json_output(data)
        else:
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

        if state.output_format == "json":
            print_json_output(data)
        else:
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

        if state.output_format == "json":
            print_json_output(data if data else {"dry_run": dry_run})
        else:
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


def _fqdn_to_exo_args(fqdn: str) -> tuple[str, str]:
    """Split a fully qualified record name into (record_name, domain).

    Example: "_acme-challenge.example.com" -> ("_acme-challenge", "example.com")
    Example: "_acme-challenge.sub.example.co.uk" -> ("_acme-challenge.sub", "example.co.uk")

    Uses a simple heuristic: the domain is the last two labels, or last
    three if the second-to-last is short (co, com, org, etc. for ccTLDs).
    """
    parts = fqdn.rstrip(".").split(".")
    if len(parts) <= 2:
        return ("", fqdn)

    # Heuristic for two-part TLDs like co.uk, com.au, org.nz
    if len(parts) >= 3 and len(parts[-2]) <= 3 and len(parts[-1]) <= 2:
        domain = ".".join(parts[-3:])
        name = ".".join(parts[:-3])
    else:
        domain = ".".join(parts[-2:])
        name = ".".join(parts[:-2])
    return (name, domain)


def _build_exo_dns_commands(data: dict) -> list[str]:
    """Build exo dns add commands from DCV params response.

    Handles three known response shapes from the Gandi API:

    1. Real API (Digicert DNS): raw_messages is a list of [name, value] pairs,
       dns_records contains BIND-format strings. We parse raw_messages.

    2. Structured fqdns: fqdns is a list of dicts with type/name/value keys.

    3. Flat: fqdns is a list of strings with top-level type/name/value.
    """
    commands = []

    # Shape 1: raw_messages — the real Gandi API shape for DNS DCV
    # Each entry is [record_name, record_value] for a CNAME record
    raw_messages = data.get("raw_messages", [])
    if raw_messages and isinstance(raw_messages[0], list) and len(raw_messages[0]) == 2:
        for pair in raw_messages:
            name = pair[0].rstrip(".")
            value = pair[1].rstrip(".")
            if name and value:
                commands.append(_format_exo_command("CNAME", name, value))
        return commands

    # Also try dns_records as fallback (BIND-format strings)
    dns_records = data.get("dns_records", [])
    if dns_records:
        for record in dns_records:
            parsed = _parse_bind_record(record)
            if parsed:
                commands.append(_format_exo_command(*parsed))
        if commands:
            return commands

    fqdns = data.get("fqdns", [])

    # Shape 2: fqdns is a list of dicts (each has type/name/value)
    if fqdns and isinstance(fqdns[0], dict):
        for entry in fqdns:
            record_type = entry.get("type", "").upper()
            fqdn = entry.get("name", "")
            value = entry.get("value", "")
            if not fqdn or not value or not record_type:
                continue
            commands.append(_format_exo_command(record_type, fqdn, value))
        return commands

    # Shape 3: fqdns is a list of strings with top-level type/name/value
    record_type = data.get("type", "CNAME").upper()
    top_name = data.get("name", "")
    top_value = data.get("value", "")
    if top_name and top_value:
        commands.append(_format_exo_command(record_type, top_name, top_value))

    return commands


def _parse_bind_record(record: str) -> tuple[str, str, str] | None:
    """Parse a BIND-format DNS record string.

    Example: '_dnsauth.cli.exoscale.org. 10800 IN CNAME _xyz.dcv.digicert.com.'
    Returns: ('CNAME', '_dnsauth.cli.exoscale.org', '_xyz.dcv.digicert.com')
    """
    parts = record.split()
    # Expected: name ttl IN type value
    if len(parts) >= 5 and parts[2].upper() == "IN":
        name = parts[0].rstrip(".")
        rtype = parts[3].upper()
        value = parts[4].rstrip(".")
        return (rtype, name, value)
    return None


def _format_exo_command(record_type: str, fqdn: str, value: str) -> str:
    """Format a single exo dns add command."""
    name, domain = _fqdn_to_exo_args(fqdn)
    if not domain:
        return f"# cannot determine domain for {fqdn}"

    if record_type == "CNAME":
        return f"exo dns add CNAME {domain} -n {name} -a {value}"
    elif record_type == "TXT":
        return f"exo dns add TXT {domain} -n {name} -c {value}"
    else:
        return f"# unsupported record type {record_type} for {fqdn} -> {value}"


@cert_app.command("set-dcv-method")
def cert_set_dcv_method(
    cert_id: Annotated[str, typer.Argument(help="Certificate ID")],
    method: Annotated[
        str,
        typer.Argument(help="DCV method: email, dns, file, http, https"),
    ],
):
    """Set the Domain Control Validation method for a certificate.

    Changes the DCV method on the certificate. Use 'cert dcv-info'
    afterwards to retrieve the validation parameters for the new method.
    """
    client = _get_client()
    try:
        client.patch(
            f"/certificate/issued-certs/{cert_id}/dcv",
            json={"method": method},
        )
        from gandi_cli.main import state

        if state.output_format == "json":
            print_json_output({"id": cert_id, "dcv_method": method})
        else:
            typer.echo(f"DCV method set to '{method}' for certificate {cert_id}.")
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
    package: Annotated[
        Optional[str],
        typer.Option("--package", help="Certificate package name"),
    ] = None,
    exo_dns: Annotated[
        bool,
        typer.Option(
            "--exo-dns",
            help="Show 'exo dns add' commands for Exoscale DNS",
        ),
    ] = False,
):
    """Get Domain Control Validation (DCV) parameters for a certificate.

    Returns the DNS record or file content needed to complete domain
    validation. Useful after 'cert set-dcv-method' to retrieve the
    validation parameters.

    With --exo-dns, prints ready-to-use 'exo dns add' commands for
    creating the required DCV records in Exoscale DNS.
    """
    client = _get_client()
    try:
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
        if package:
            body["package"] = package

        data = client.post(
            f"/certificate/issued-certs/{cert_id}/dcv_params",
            json=body,
        )
        from gandi_cli.main import state

        if exo_dns:
            dcv_data = data if isinstance(data, dict) else {}
            commands = _build_exo_dns_commands(dcv_data)
            if state.output_format == "json":
                print_json_output({"commands": commands})
            elif commands:
                for cmd in commands:
                    typer.echo(cmd)
            else:
                typer.echo("No DNS records to create.", err=True)
        else:
            output(data, fmt=state.output_format)
    except GandiAPIError as e:
        typer.echo(f"Error: {e}", err=True)
        raise typer.Exit(1)


def _package_to_pem_type(package_name: str) -> str:
    """Derive the intermediate cert type from a package name.

    Package names look like 'cert_std_1_10_0_digicert' or 'cert_bus_1_0_0'.
    The PEM type is the prefix before the version digits, e.g. 'cert_std'.
    """
    parts = package_name.split("_")
    # Walk until we hit a digit — everything before that is the type.
    prefix_parts = []
    for part in parts:
        if part.isdigit():
            break
        prefix_parts.append(part)
    return "_".join(prefix_parts) if prefix_parts else package_name


@cert_app.command("download")
def cert_download(
    cert_id: Annotated[str, typer.Argument(help="Certificate ID")],
    output_dir: Annotated[
        Path,
        typer.Option("--output-dir", "-d", help="Directory for the .crt file"),
    ] = Path("."),
):
    """Download the certificate chain (domain + intermediate) as a PEM file.

    Fetches the issued certificate and the matching intermediate
    certificate, concatenates them, and writes the result to
    OUTPUT_DIR/DOMAIN.crt (where DOMAIN is the certificate CN).
    """
    client = _get_client()
    try:
        # 1. Fetch cert details to get CN and package name
        info = client.get(f"/certificate/issued-certs/{cert_id}")
        cn = info.get("cn", "")
        if not cn:
            typer.echo("Error: certificate has no CN.", err=True)
            raise typer.Exit(1)
        pkg = info.get("package", {})
        package_name = pkg.get("name", "") if isinstance(pkg, dict) else str(pkg)
        if not package_name:
            typer.echo("Error: certificate has no package name.", err=True)
            raise typer.Exit(1)

        pem_type = _package_to_pem_type(package_name)

        # 2. Fetch domain cert
        domain_pem = client.get(
            f"/certificate/issued-certs/{cert_id}/crt",
            headers={"Accept": "text/plain"},
        )
        domain_pem = domain_pem if isinstance(domain_pem, str) else str(domain_pem)

        # 3. Fetch intermediate cert
        intermediate_pem = client.get(
            f"/certificate/pem/{pem_type}",
            headers={"Accept": "text/plain"},
        )
        intermediate_pem = intermediate_pem if isinstance(intermediate_pem, str) else str(intermediate_pem)

        # 4. Concatenate and write
        chain = domain_pem.rstrip("\n") + "\n" + intermediate_pem.rstrip("\n") + "\n"

        output_dir.mkdir(parents=True, exist_ok=True)
        out_file = output_dir / f"{cn}.crt"

        from gandi_cli.main import state

        if state.output_format == "json":
            print_json_output({
                "id": cert_id,
                "cn": cn,
                "file": str(out_file),
                "certificate": chain,
            })
        else:
            out_file.write_text(chain)
            typer.echo(f"Certificate chain written to {out_file}")
    except GandiAPIError as e:
        typer.echo(f"Error: {e}", err=True)
        raise typer.Exit(1)


@cert_app.command("revoke")
def cert_revoke(
    cert_id: Annotated[str, typer.Argument(help="Certificate ID")],
    force: Annotated[
        bool,
        typer.Option("--force", "-f", help="Skip confirmation prompt"),
    ] = False,
):
    """Revoke a certificate.

    This permanently revokes the certificate. The operation cannot be
    undone. You will be prompted for confirmation unless --force is used.
    """
    if not force:
        confirm = typer.confirm(
            f"Revoke certificate {cert_id}? This cannot be undone."
        )
        if not confirm:
            typer.echo("Aborted.")
            raise typer.Exit(0)

    client = _get_client()
    try:
        client.delete(f"/certificate/issued-certs/{cert_id}")
        from gandi_cli.main import state

        if state.output_format == "json":
            print_json_output({"id": cert_id, "status": "revoked"})
        else:
            typer.echo(f"Certificate {cert_id} has been revoked.")
    except GandiAPIError as e:
        typer.echo(f"Error: {e}", err=True)
        raise typer.Exit(1)
