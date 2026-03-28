"""Organization management commands."""

from typing import Annotated, Optional

import typer

from gandi_cli.client import GandiClient, GandiAPIError
from gandi_cli.output import output

org_app = typer.Typer(help="Organization management", no_args_is_help=True)


def _get_client() -> GandiClient:
    from gandi_cli.main import state

    if not state.token:
        typer.echo(
            "Error: No API token. Run 'gandi-v5 auth login' or set GANDI_PAT.",
            err=True,
        )
        raise typer.Exit(1)
    return GandiClient(token=state.token, sharing_id=state.sharing_id, sandbox=state.sandbox)


@org_app.command("list")
def org_list(
    name: Annotated[
        Optional[str], typer.Option(help="Filter by name")
    ] = None,
    per_page: Annotated[int, typer.Option(help="Items per page")] = 25,
    page: Annotated[int, typer.Option(help="Page number")] = 1,
):
    """List organizations."""
    client = _get_client()
    params: dict = {"page": page, "per_page": per_page}
    if name:
        params["name"] = name
    try:
        data = client.get("/organization/organizations", params=params)
        from gandi_cli.main import state

        columns = [
            ("id", "ID"),
            ("name", "Name"),
            ("type", "Type"),
        ]
        output(data, fmt=state.output_format, columns=columns, title="Organizations")
    except GandiAPIError as e:
        typer.echo(f"Error: {e}", err=True)
        raise typer.Exit(1)


@org_app.command("info")
def org_info(
    org_id: Annotated[str, typer.Argument(help="Organization ID")],
):
    """Show organization details."""
    client = _get_client()
    try:
        data = client.get(f"/organization/organizations/{org_id}")
        from gandi_cli.main import state

        fields = [
            ("id", "ID"),
            ("name", "Name"),
            ("type", "Type"),
            ("orgname", "Org Name"),
            ("email", "Email"),
            ("vat_number", "VAT"),
            ("corporate", "Corporate"),
        ]
        output(data, fmt=state.output_format, detail_fields=fields)
    except GandiAPIError as e:
        typer.echo(f"Error: {e}", err=True)
        raise typer.Exit(1)


@org_app.command("whoami")
def whoami():
    """Show current authenticated user info."""
    client = _get_client()
    try:
        data = client.get("/organization/user-info")
        from gandi_cli.main import state

        fields = [
            ("username", "Username"),
            ("email", "Email"),
            ("firstname", "First Name"),
            ("lastname", "Last Name"),
            ("id", "ID"),
            ("lang", "Language"),
        ]
        output(data, fmt=state.output_format, detail_fields=fields)
    except GandiAPIError as e:
        typer.echo(f"Error: {e}", err=True)
        raise typer.Exit(1)
