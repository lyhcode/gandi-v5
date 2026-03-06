"""Authentication management commands."""

from typing import Annotated, Optional

import typer
from rich.console import Console

from gandi_cli.config import load_config, save_config, get_config_path

console = Console()
auth_app = typer.Typer(help="Authentication management", no_args_is_help=True)


@auth_app.command("login")
def login(
    token: Annotated[Optional[str], typer.Option("--token", "-t", help="Personal Access Token")] = None,
):
    """Save your Gandi Personal Access Token (PAT)."""
    if token is None:
        token = typer.prompt("Enter your Gandi Personal Access Token (PAT)", hide_input=True)
    if not token:
        console.print("[red]Error: Token cannot be empty[/red]")
        raise typer.Exit(1)
    config = load_config()
    config.auth.pat = token
    save_config(config)
    console.print(f"[green]Token saved to {get_config_path()}[/green]")


@auth_app.command("logout")
def logout():
    """Remove saved authentication token."""
    config = load_config()
    if not config.auth.pat:
        console.print("No token configured.")
        return
    config.auth.pat = ""
    save_config(config)
    console.print("[green]Token removed.[/green]")


@auth_app.command("status")
def status():
    """Show current authentication status."""
    import os

    config = load_config()
    token = os.environ.get("GANDI_PAT") or config.auth.pat
    source = "env:GANDI_PAT" if os.environ.get("GANDI_PAT") else "config"

    if token:
        masked = token[:8] + "..." + token[-4:] if len(token) > 12 else "***"
        console.print(f"Token:      {masked} (from {source})")
    else:
        console.print("[yellow]No token configured[/yellow]")
        console.print("Run 'gandi auth login' or set GANDI_PAT environment variable")

    console.print(f"Config:     {get_config_path()}")

    if config.defaults.sharing_id:
        console.print(f"Sharing ID: {config.defaults.sharing_id}")
    console.print(f"Output:     {config.defaults.output}")


@auth_app.command("set-org")
def set_org(
    org_id: Annotated[str, typer.Argument(help="Organization sharing ID")],
):
    """Set the default organization (sharing_id) for API requests."""
    config = load_config()
    config.defaults.sharing_id = org_id
    save_config(config)
    console.print(f"[green]Default organization set to: {org_id}[/green]")
