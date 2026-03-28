"""LiveDNS record management commands."""

from typing import Annotated, Optional

import typer

from gandi_cli.client import GandiClient, GandiAPIError
from gandi_cli.output import output

dns_app = typer.Typer(help="LiveDNS record management", no_args_is_help=True)


def _get_client() -> GandiClient:
    from gandi_cli.main import state

    if not state.token:
        typer.echo(
            "Error: No API token. Run 'gandi-v5 auth login' or set GANDI_PAT.",
            err=True,
        )
        raise typer.Exit(1)
    return GandiClient(token=state.token, sharing_id=state.sharing_id, sandbox=state.sandbox)


@dns_app.command("list")
def dns_list(
    domain: Annotated[str, typer.Argument(help="Domain name")],
    rrset_type: Annotated[
        Optional[str],
        typer.Option("--type", "-t", help="Filter by record type (A, AAAA, CNAME, ...)"),
    ] = None,
    name: Annotated[
        Optional[str],
        typer.Option("--name", "-n", help="Filter by record name"),
    ] = None,
):
    """List DNS records for a domain."""
    client = _get_client()
    try:
        data = client.get(f"/livedns/domains/{domain}/records")
        # Apply filters client-side if specified
        if rrset_type:
            data = [r for r in data if r.get("rrset_type") == rrset_type.upper()]
        if name:
            data = [r for r in data if r.get("rrset_name") == name]
        from gandi_cli.main import state

        columns = [
            ("rrset_name", "Name"),
            ("rrset_type", "Type"),
            ("rrset_ttl", "TTL"),
            ("rrset_values", "Values"),
        ]
        # Flatten values list to comma-separated string
        for item in data:
            vals = item.get("rrset_values", [])
            item["rrset_values"] = ", ".join(vals) if isinstance(vals, list) else str(vals)
        output(data, fmt=state.output_format, columns=columns, title=f"DNS Records: {domain}")
    except GandiAPIError as e:
        typer.echo(f"Error: {e}", err=True)
        raise typer.Exit(1)


@dns_app.command("get")
def dns_get(
    domain: Annotated[str, typer.Argument(help="Domain name")],
    name: Annotated[str, typer.Argument(help="Record name (e.g., www, @)")],
    rrset_type: Annotated[
        str, typer.Argument(help="Record type (A, AAAA, CNAME, TXT, MX, ...)")
    ],
):
    """Get a specific DNS record."""
    client = _get_client()
    try:
        data = client.get(
            f"/livedns/domains/{domain}/records/{name}/{rrset_type.upper()}"
        )
        from gandi_cli.main import state

        fields = [
            ("rrset_name", "Name"),
            ("rrset_type", "Type"),
            ("rrset_ttl", "TTL"),
            ("rrset_values", "Values"),
        ]
        data["rrset_values"] = ", ".join(data.get("rrset_values", []))
        output(data, fmt=state.output_format, detail_fields=fields)
    except GandiAPIError as e:
        typer.echo(f"Error: {e}", err=True)
        raise typer.Exit(1)


@dns_app.command("create")
def dns_create(
    domain: Annotated[str, typer.Argument(help="Domain name")],
    name: Annotated[str, typer.Argument(help="Record name (e.g., www, @)")],
    rrset_type: Annotated[
        str, typer.Argument(help="Record type (A, AAAA, CNAME, TXT, MX, ...)")
    ],
    values: Annotated[list[str], typer.Argument(help="Record values")],
    ttl: Annotated[int, typer.Option(help="TTL in seconds")] = 10800,
):
    """Create a new DNS record."""
    client = _get_client()
    body = {
        "rrset_name": name,
        "rrset_type": rrset_type.upper(),
        "rrset_ttl": ttl,
        "rrset_values": values,
    }
    try:
        client.post(f"/livedns/domains/{domain}/records", json=body)
        typer.echo(f"Created {rrset_type.upper()} record '{name}' for {domain}")
    except GandiAPIError as e:
        typer.echo(f"Error: {e}", err=True)
        raise typer.Exit(1)


@dns_app.command("update")
def dns_update(
    domain: Annotated[str, typer.Argument(help="Domain name")],
    name: Annotated[str, typer.Argument(help="Record name")],
    rrset_type: Annotated[str, typer.Argument(help="Record type")],
    values: Annotated[
        list[str],
        typer.Option("--value", "-v", help="New record values (repeat for multiple)"),
    ] = None,
    ttl: Annotated[Optional[int], typer.Option(help="New TTL in seconds")] = None,
):
    """Update an existing DNS record."""
    if not values:
        typer.echo("Error: At least one --value is required.", err=True)
        raise typer.Exit(1)
    client = _get_client()
    body = {"rrset_values": values}
    if ttl is not None:
        body["rrset_ttl"] = ttl
    try:
        client.put(
            f"/livedns/domains/{domain}/records/{name}/{rrset_type.upper()}",
            json=body,
        )
        typer.echo(f"Updated {rrset_type.upper()} record '{name}' for {domain}")
    except GandiAPIError as e:
        typer.echo(f"Error: {e}", err=True)
        raise typer.Exit(1)


@dns_app.command("delete")
def dns_delete(
    domain: Annotated[str, typer.Argument(help="Domain name")],
    name: Annotated[str, typer.Argument(help="Record name")],
    rrset_type: Annotated[str, typer.Argument(help="Record type")],
    force: Annotated[
        bool, typer.Option("--force", "-f", help="Skip confirmation")
    ] = False,
):
    """Delete a DNS record."""
    if not force:
        confirm = typer.confirm(
            f"Delete {rrset_type.upper()} record '{name}' for {domain}?"
        )
        if not confirm:
            typer.echo("Cancelled.")
            raise typer.Exit(0)
    client = _get_client()
    try:
        client.delete(
            f"/livedns/domains/{domain}/records/{name}/{rrset_type.upper()}"
        )
        typer.echo(f"Deleted {rrset_type.upper()} record '{name}' from {domain}")
    except GandiAPIError as e:
        typer.echo(f"Error: {e}", err=True)
        raise typer.Exit(1)


@dns_app.command("export")
def dns_export(
    domain: Annotated[str, typer.Argument(help="Domain name")],
):
    """Export DNS records as zone file (text format)."""
    client = _get_client()
    try:
        data = client.get(
            f"/livedns/domains/{domain}/records",
            headers={"Accept": "text/plain"},
        )
        typer.echo(data)
    except GandiAPIError as e:
        typer.echo(f"Error: {e}", err=True)
        raise typer.Exit(1)
