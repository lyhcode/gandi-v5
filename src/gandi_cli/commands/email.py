from typing import Annotated, Optional
import typer
from gandi_cli.client import GandiClient, GandiAPIError
from gandi_cli.output import output

email_app = typer.Typer(help="Email management", no_args_is_help=True)
forward_app = typer.Typer(help="Email forwarding management", no_args_is_help=True)
mailbox_app = typer.Typer(help="Mailbox management", no_args_is_help=True)
email_app.add_typer(forward_app, name="forward")
email_app.add_typer(mailbox_app, name="mailbox")

def _get_client():
    from gandi_cli.main import state
    if not state.token:
        typer.echo("Error: No API token.", err=True)
        raise typer.Exit(1)
    return GandiClient(token=state.token, sharing_id=state.sharing_id, sandbox=state.sandbox)

@forward_app.command("list")
def forward_list(
    domain: Annotated[str, typer.Argument(help="Domain name")],
    per_page: Annotated[int, typer.Option(help="Items per page")] = 25,
    page: Annotated[int, typer.Option(help="Page number")] = 1,
):
    """List email forwards for a domain."""
    client = _get_client()
    params = {"page": page, "per_page": per_page}
    try:
        data = client.get(f"/email/forwards/{domain}", params=params)
        from gandi_cli.main import state
        columns = [
            ("source", "Source"),
            ("destinations", "Destinations"),
        ]
        for item in data:
            dests = item.get("destinations", [])
            item["destinations"] = ", ".join(dests) if isinstance(dests, list) else str(dests)
        output(data, fmt=state.output_format, columns=columns, title=f"Forwards: {domain}")
    except GandiAPIError as e:
        typer.echo(f"Error: {e}", err=True)
        raise typer.Exit(1)

@forward_app.command("create")
def forward_create(
    domain: Annotated[str, typer.Argument(help="Domain name")],
    source: Annotated[str, typer.Argument(help="Source address (local part)")],
    destinations: Annotated[list[str], typer.Argument(help="Destination email addresses")],
):
    """Create an email forward."""
    client = _get_client()
    body = {"source": source, "destinations": destinations}
    try:
        client.post(f"/email/forwards/{domain}", json=body)
        typer.echo(f"Created forward: {source}@{domain} -> {', '.join(destinations)}")
    except GandiAPIError as e:
        typer.echo(f"Error: {e}", err=True)
        raise typer.Exit(1)

@forward_app.command("delete")
def forward_delete(
    domain: Annotated[str, typer.Argument(help="Domain name")],
    source: Annotated[str, typer.Argument(help="Source address to delete")],
    force: Annotated[bool, typer.Option("--force", "-f", help="Skip confirmation")] = False,
):
    """Delete an email forward."""
    if not force:
        confirm = typer.confirm(f"Delete forward {source}@{domain}?")
        if not confirm:
            raise typer.Exit(0)
    client = _get_client()
    try:
        client.delete(f"/email/forwards/{domain}/{source}")
        typer.echo(f"Deleted forward: {source}@{domain}")
    except GandiAPIError as e:
        typer.echo(f"Error: {e}", err=True)
        raise typer.Exit(1)

@mailbox_app.command("list")
def mailbox_list(
    domain: Annotated[str, typer.Argument(help="Domain name")],
    per_page: Annotated[int, typer.Option(help="Items per page")] = 25,
    page: Annotated[int, typer.Option(help="Page number")] = 1,
):
    """List mailboxes for a domain."""
    client = _get_client()
    params = {"page": page, "per_page": per_page}
    try:
        data = client.get(f"/email/mailboxes/{domain}", params=params)
        from gandi_cli.main import state
        columns = [
            ("id", "ID"),
            ("address", "Address"),
            ("mailbox_type", "Type"),
            ("quota_used", "Quota Used"),
        ]
        for item in data:
            item["address"] = item.get("address", item.get("login", ""))
        output(data, fmt=state.output_format, columns=columns, title=f"Mailboxes: {domain}")
    except GandiAPIError as e:
        typer.echo(f"Error: {e}", err=True)
        raise typer.Exit(1)

@mailbox_app.command("info")
def mailbox_info(
    domain: Annotated[str, typer.Argument(help="Domain name")],
    mailbox_id: Annotated[str, typer.Argument(help="Mailbox ID")],
):
    """Show mailbox details."""
    client = _get_client()
    try:
        data = client.get(f"/email/mailboxes/{domain}/{mailbox_id}")
        from gandi_cli.main import state
        fields = [
            ("id", "ID"),
            ("address", "Address"),
            ("mailbox_type", "Type"),
            ("quota_used", "Quota Used"),
            ("aliases", "Aliases"),
            ("expires_at", "Expires"),
        ]
        data["address"] = data.get("address", data.get("login", ""))
        data["aliases"] = ", ".join(data.get("aliases", []))
        output(data, fmt=state.output_format, detail_fields=fields)
    except GandiAPIError as e:
        typer.echo(f"Error: {e}", err=True)
        raise typer.Exit(1)
