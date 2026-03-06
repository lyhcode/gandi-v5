"""Gandi CLI entry point."""

from typing import Annotated, Optional

import typer

from gandi_cli.config import load_config
from gandi_cli.commands.auth import auth_app
from gandi_cli.commands.dns import dns_app
from gandi_cli.commands.domain import domain_app
from gandi_cli.commands.organization import org_app
from gandi_cli.commands.certificate import cert_app
from gandi_cli.commands.email import email_app

app = typer.Typer(name="gandi", help="Gandi.net CLI tool", no_args_is_help=True)
app.add_typer(auth_app, name="auth")
app.add_typer(cert_app, name="cert")
app.add_typer(dns_app, name="dns")
app.add_typer(domain_app, name="domain")
app.add_typer(email_app, name="email")
app.add_typer(org_app, name="org")


# Global state
class State:
    token: str | None = None
    sharing_id: str | None = None
    output_format: str = "table"
    sandbox: bool = False


state = State()


@app.callback()
def main(
    output: Annotated[str, typer.Option("--output", "-o", help="Output format: table, json, plain")] = "",
    token: Annotated[Optional[str], typer.Option("--token", envvar="GANDI_PAT", help="API token")] = None,
    sharing_id: Annotated[Optional[str], typer.Option("--sharing-id", envvar="GANDI_SHARING_ID", help="Organization sharing ID")] = None,
    sandbox: Annotated[bool, typer.Option("--sandbox", help="Use Gandi Sandbox API (api.sandbox.gandi.net)")] = False,
):
    config = load_config()
    state.token = token or config.auth.pat or None
    state.sharing_id = sharing_id or config.defaults.sharing_id or None
    state.output_format = output or config.defaults.output
    state.sandbox = sandbox


if __name__ == "__main__":
    app()
