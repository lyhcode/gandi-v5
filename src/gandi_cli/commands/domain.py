"""Domain management commands."""

from typing import Annotated, Optional

import typer

from gandi_cli.client import GandiClient, GandiAPIError
from gandi_cli.output import output

domain_app = typer.Typer(help="Domain management", no_args_is_help=True)


def _get_client() -> GandiClient:
    from gandi_cli.main import state

    if not state.token:
        typer.echo(
            "Error: No API token. Run 'gandi auth login' or set GANDI_PAT.",
            err=True,
        )
        raise typer.Exit(1)
    return GandiClient(token=state.token, sharing_id=state.sharing_id, sandbox=state.sandbox)


@domain_app.command("list")
def domain_list(
    fqdn: Annotated[
        Optional[str], typer.Option(help="Filter by FQDN pattern")
    ] = None,
    page: Annotated[int, typer.Option(help="Page number")] = 1,
    per_page: Annotated[int, typer.Option(help="Items per page")] = 25,
):
    """List your domains."""
    client = _get_client()
    params: dict = {"page": page, "per_page": per_page}
    if fqdn:
        params["fqdn"] = fqdn
    try:
        data = client.get("/domain/domains", params=params)
        from gandi_cli.main import state

        columns = [
            ("fqdn", "Domain"),
            ("status", "Status"),
            ("dates.registry_ends_at", "Expires"),
            ("autorenew", "Autorenew"),
        ]
        # Flatten nested dates for table display
        for item in data:
            dates = item.get("dates", {})
            item["dates.registry_ends_at"] = (
                dates.get("registry_ends_at") or ""
            )[:10]
            item["autorenew"] = "Yes" if item.get("autorenew") else "No"
        output(data, fmt=state.output_format, columns=columns, title="Domains")
    except GandiAPIError as e:
        typer.echo(f"Error: {e}", err=True)
        raise typer.Exit(1)


@domain_app.command("info")
def domain_info(
    domain: Annotated[str, typer.Argument(help="Domain name (FQDN)")],
):
    """Show detailed information about a domain."""
    client = _get_client()
    try:
        data = client.get(f"/domain/domains/{domain}")
        from gandi_cli.main import state

        fields = [
            ("fqdn", "Domain"),
            ("status", "Status"),
            ("tld", "TLD"),
            ("owner", "Owner"),
            ("orga_owner", "Organization"),
            ("nameservers", "Nameservers"),
            ("autorenew", "Autorenew"),
            ("dates", "Dates"),
            ("tags", "Tags"),
        ]
        # Format autorenew
        data["autorenew"] = "Yes" if data.get("autorenew") else "No"
        data["nameservers"] = ", ".join(data.get("nameservers", []))
        dates = data.get("dates", {})
        date_lines = []
        for k, v in dates.items():
            if v:
                date_lines.append(f"{k}: {v[:10]}")
        data["dates"] = ", ".join(date_lines)
        output(data, fmt=state.output_format, detail_fields=fields)
    except GandiAPIError as e:
        typer.echo(f"Error: {e}", err=True)
        raise typer.Exit(1)


@domain_app.command("check")
def domain_check(
    name: Annotated[
        str, typer.Argument(help="Domain name to check availability")
    ],
    currency: Annotated[
        Optional[str],
        typer.Option(help="Currency code (e.g., USD, EUR, TWD)"),
    ] = None,
):
    """Check domain availability and pricing."""
    client = _get_client()
    params: dict = {"name": name}
    if currency:
        params["currency"] = currency
    try:
        data = client.get("/domain/check", params=params)
        from gandi_cli.main import state

        products = data.get("products", [])
        if not products:
            typer.echo(f"{name}: No results")
            return
        # Show availability info
        for product in products:
            status = product.get("status", "unknown")
            prices = product.get("prices", [])
            price_info = ""
            for p in prices:
                if p.get("duration_unit") == "y":
                    price_info = (
                        f" - {p.get('price_after_taxes', 'N/A')}"
                        f" {data.get('currency', '')}"
                        f" / {p.get('duration', 1)}yr"
                    )
                    break
            typer.echo(f"{name}: {status}{price_info}")
    except GandiAPIError as e:
        typer.echo(f"Error: {e}", err=True)
        raise typer.Exit(1)
