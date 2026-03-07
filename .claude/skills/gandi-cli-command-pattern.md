# Skill: Adding New CLI Commands to gandi-cli

## When to use
Use this skill when adding new commands or subcommands to the gandi-cli project.

## Project Structure
- Entry point: `src/gandi_cli/main.py` — Typer app with global `State` class
- Commands: `src/gandi_cli/commands/<module>.py` — one file per API area
- HTTP client: `src/gandi_cli/client.py` — `GandiClient` wrapping httpx
- Output: `src/gandi_cli/output.py` — `output()` dispatcher for table/json/plain
- Config: `src/gandi_cli/config.py` — TOML config at `~/.config/gandi-cli/config.toml`
- Tests: `tests/test_<module>.py` with `pytest-httpx` for mocking

## Command Module Pattern

Every command module follows this structure:

```python
from typing import Annotated, Optional
import typer
from gandi_cli.client import GandiClient, GandiAPIError
from gandi_cli.output import output

# Create Typer app (use sub-typers for nested commands)
my_app = typer.Typer(help="Description", no_args_is_help=True)

# Private helper to get authenticated client
def _get_client() -> GandiClient:
    from gandi_cli.main import state  # lazy import to avoid circular
    if not state.token:
        typer.echo("Error: No API token. Run 'gandi auth login' or set GANDI_PAT.", err=True)
        raise typer.Exit(1)
    return GandiClient(token=state.token, sharing_id=state.sharing_id, sandbox=state.sandbox)

# List command (returns table)
@my_app.command("list")
def my_list(
    domain: Annotated[str, typer.Argument(help="Domain name")],
    per_page: Annotated[int, typer.Option(help="Items per page")] = 25,
    page: Annotated[int, typer.Option(help="Page number")] = 1,
):
    """List items."""
    client = _get_client()
    try:
        data = client.get(f"/api/path/{domain}", params={"page": page, "per_page": per_page})
        from gandi_cli.main import state
        columns = [("field", "Header"), ...]
        output(data, fmt=state.output_format, columns=columns, title="Title")
    except GandiAPIError as e:
        typer.echo(f"Error: {e}", err=True)
        raise typer.Exit(1)

# Detail command (returns key-value)
@my_app.command("info")
def my_info(
    item_id: Annotated[str, typer.Argument(help="Item ID")],
):
    """Show item details."""
    client = _get_client()
    try:
        data = client.get(f"/api/path/{item_id}")
        from gandi_cli.main import state
        fields = [("key", "Label"), ...]
        output(data, fmt=state.output_format, detail_fields=fields)
    except GandiAPIError as e:
        typer.echo(f"Error: {e}", err=True)
        raise typer.Exit(1)

# Mutating commands (create/update/delete)
@my_app.command("create")
def my_create(...):
    client = _get_client()
    body = {"key": "value"}
    try:
        client.post("/api/path", json=body)
        typer.echo("Success message")
    except GandiAPIError as e:
        typer.echo(f"Error: {e}", err=True)
        raise typer.Exit(1)

# Delete with confirmation
@my_app.command("delete")
def my_delete(
    item_id: Annotated[str, typer.Argument(help="Item ID")],
    force: Annotated[bool, typer.Option("--force", "-f", help="Skip confirmation")] = False,
):
    if not force:
        if not typer.confirm(f"Delete {item_id}?"):
            raise typer.Exit(0)
    client = _get_client()
    try:
        client.delete(f"/api/path/{item_id}")
        typer.echo(f"Deleted {item_id}")
    except GandiAPIError as e:
        typer.echo(f"Error: {e}", err=True)
        raise typer.Exit(1)
```

## Registering Commands in main.py

```python
from gandi_cli.commands.my_module import my_app
app.add_typer(my_app, name="my-command")
```

## Nested Sub-commands (e.g., `gandi email forward list`)

```python
email_app = typer.Typer(help="Email management", no_args_is_help=True)
forward_app = typer.Typer(help="Forwarding", no_args_is_help=True)
email_app.add_typer(forward_app, name="forward")
```

## Output Conventions
- `output(data, fmt=state.output_format, columns=[...])` for lists (table)
- `output(data, fmt=state.output_format, detail_fields=[...])` for single records
- Flatten nested lists/dicts before passing to output (e.g., join list values with ", ")

## GandiClient Methods
- `client.get(path, params=None, headers=None)` — sharing_id auto-injected
- `client.post(path, json=None, params=None)`
- `client.put(path, json=None, params=None)`
- `client.patch(path, json=None, params=None)`
- `client.delete(path, params=None)`
- Base URL: `https://api.gandi.net/v5` (or sandbox variant)
- Auth: Bearer PAT token in header

## Test Pattern

```python
import pytest
from typer.testing import CliRunner
from gandi_cli.main import app

runner = CliRunner()

@pytest.fixture
def mock_client(httpx_mock):
    # Mock _get_client to return a real GandiClient pointing at mock
    ...

def test_my_list(httpx_mock):
    httpx_mock.add_response(url=..., json=[...])
    result = runner.invoke(app, ["my-command", "list", ...])
    assert result.exit_code == 0
```

## API Documentation
Refer to `docs/` directory for complete Gandi API endpoint specs:
- `docs/domain-api.md` — Domain management
- `docs/livedns-api.md` — DNS records
- `docs/email-api.md` — Email forwards/mailboxes
- `docs/certificate-api.md` — SSL certificates
- `docs/organization-api.md` — Organizations
- `docs/billing-api.md` — Billing
