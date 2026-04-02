# gandi-v5 Project Summary

## File-by-File Breakdown

### 1. `src/gandi_cli/client.py` — HTTP API Client
- **`GandiAPIError`**: Custom exception with `status_code`, `cause`, `message`, `object` fields.
- **`GandiClient`**: Wraps `httpx.Client` with:
  - `BASE_URL = "https://api.gandi.net/v5"`, `SANDBOX_URL = "https://api.sandbox.gandi.net/v5"`
  - Constructor: `token`, `sharing_id`, `timeout=30.0`, `sandbox=False`
  - Auth: `Authorization: Bearer {token}` header
  - `_inject_sharing_id()`: Auto-adds `sharing_id` to query params (GET and POST only currently)
  - `_handle_response()`: Returns JSON/text, raises `GandiAPIError` for 4xx/5xx, returns `{}` for 204
  - Methods: `get()`, `post()`, `put()`, `patch()`, `delete()`, `close()`
  - Context manager support (`__enter__`/`__exit__`)
  - **Note**: `put()`, `patch()`, `delete()` do NOT call `_inject_sharing_id()` (potential oversight)

### 2. `src/gandi_cli/commands/certificate.py` — Certificate Commands
- **`cert_app`**: Typer app with `no_args_is_help=True`
- **`_get_client()`**: Lazy-imports `state` from `main`, creates `GandiClient`
- **`cert_list`** (`gandi cert list`):
  - Options: `--cn`, `--status`, `--per-page` (default 25), `--page` (default 1)
  - Endpoint: `GET /certificate/issued-certs`
  - Flattens `dates.ends_at` (truncated to 10 chars) and `package.name` for table display
  - Columns: ID, Common Name, Status, Expires, Package
- **`cert_info`** (`gandi cert info <cert_id>`):
  - Argument: `cert_id`
  - Endpoint: `GET /certificate/issued-certs/{cert_id}`
  - Flattens altnames (joined with ", "), package name, date fields
  - Fields: ID, Common Name, Status, Alt Names, Package, Valid From, Valid Until

### 3. `src/gandi_cli/main.py` — CLI Entry Point
- **`app`**: Root Typer app (`name="gandi-v5"`)
- **Registered sub-apps**: `auth`, `cert`, `dns`, `domain`, `email`, `org`
- **`State` class**: Global singleton holding `token`, `sharing_id`, `output_format`, `sandbox`
- **`main()` callback**: Resolves config via `load_config()`, sets state from CLI options → env vars → config file
  - `--output/-o`: table/json/plain
  - `--token` (envvar `GANDI_PAT`)
  - `--sharing-id` (envvar `GANDI_SHARING_ID`)
  - `--sandbox`: Use sandbox API

### 4. `src/gandi_cli/output.py` — Output Formatting
- **`print_table()`**: Rich table with columns defined as `(key, header)` tuples
- **`print_json_output()`**: Pretty JSON via Rich
- **`print_plain()`**: Tab-separated key=value for lists, key: value for dicts
- **`print_detail()`**: Rich key-value table (no header, bold cyan field names)
- **`output()`**: Universal dispatcher:
  - `fmt="json"` → `print_json_output()`
  - `fmt="plain"` → `print_plain()`
  - `fmt="table"` (default) → `print_table()` for lists with columns, `print_detail()` for dicts

### 5. `src/gandi_cli/config.py` — Configuration Management
- **Pydantic models**: `AuthConfig(pat)`, `DefaultsConfig(sharing_id, output)`, `GandiConfig(auth, defaults)`
- **Config path**: `~/.config/gandi-cli/config.toml` (via platformdirs)
- **`load_config()`**: Reads TOML, returns `GandiConfig` (default if missing)
- **`save_config()`**: Writes TOML via `tomli_w`
- **`get_token()`**: Priority: override → `GANDI_PAT` env → config file (exits if none)
- **`get_sharing_id()`**: Priority: override → `GANDI_SHARING_ID` env → config file

### 6. `src/gandi_cli/models/__init__.py` — Empty
### 7. `src/gandi_cli/commands/__init__.py` — Empty

### 8. `pyproject.toml` — Build Configuration
- Build: hatchling
- Entry point: `gandi-v5 = "gandi_cli.main:app"`
- Python: >=3.11
- Dependencies: typer, rich, httpx, pydantic, platformdirs, tomli-w
- Dev dependencies: pytest, pytest-httpx (>=0.30.0), pytest-cov

### 9. `skills/gandi-cli-command-pattern.md` — Command Development Guide
- Documents the standard pattern for all command modules
- Shows `_get_client()` helper, list/info/create/delete patterns
- Explains output conventions, client methods, and test patterns
- References nested sub-commands (e.g., `email forward`)

### 10. `skills/gandi-api-certificate.md` — Certificate API Reference
- **Implemented**: `cert list`, `cert info`
- **Not yet implemented**:
  - `POST /v5/certificate/issued-certs` — Order new certificate (CSR + package + dcv_method)
  - `PATCH /v5/certificate/issued-certs/{id}` — Reissue certificate
  - `DELETE /v5/certificate/issued-certs/{id}` — Revoke certificate
  - `GET /v5/certificate/issued-certs/{id}/dcv` — Check DCV status
  - `GET /v5/certificate/packages` — List certificate packages
  - `GET /v5/certificate/packages/{name}` — Get package info
- Business rules: CSR required, DCV methods (dns/email/http/cname), package types (std/pro/business)

### 11. `tests/test_commands/test_certificate.py` — Certificate Tests
- Uses `CliRunner` from typer.testing
- Creates a wrapper Typer app with `cert_app` added as sub-typer
- **Mocking pattern**: `patch("gandi_cli.commands.certificate._get_client")` returns `GandiClient(token="test-token")`, while `httpx_mock` (pytest-httpx) intercepts the actual HTTP calls
- **`TestCertList`** (6 tests): list output contains CNs, IDs, statuses, expiry dates, package names; cn/status filter params sent correctly
- **`TestCertInfo`** (5 tests): info shows cert-001, CN, status, altnames, dates, package; correct URL requested

### 12. `tests/fixtures/certificates.json` — List Fixture
- 2 certificates: cert-001 (example.com, valid, expires 2025-01-01) and cert-002 (shop.example.com, expired, expires 2024-06-15)
- Both have `package: {"name": "std_dv_1y"}`

### 13. `tests/fixtures/certificate_detail.json` — Detail Fixture
- cert-001 with altnames ["www.example.com", "mail.example.com"]

### 14. `tests/conftest.py` — Shared Test Fixtures
- `cli_runner`: CliRunner instance
- `mock_config`: Patches `load_config` to return test config with token "test-token-123"
- `load_fixture()`: Helper to read JSON fixtures

---

## Overall Architecture Summary

### CLI Structure (Click/Typer Groups)
```
gandi (root Typer app)
├── auth     → auth_app    (gandi_cli.commands.auth)
├── cert     → cert_app    (gandi_cli.commands.certificate)
├── dns      → dns_app     (gandi_cli.commands.dns)
├── domain   → domain_app  (gandi_cli.commands.domain)
├── email    → email_app   (gandi_cli.commands.email)
└── org      → org_app     (gandi_cli.commands.organization)
```
- Each command module exports a `Typer()` instance (e.g., `cert_app`)
- Registered in `main.py` via `app.add_typer(cert_app, name="cert")`
- Global `State` singleton holds auth/config, populated by the `@app.callback()` before any subcommand runs

### API Client
- **Auth**: Bearer PAT token in `Authorization` header
- **Base URL**: `https://api.gandi.net/v5` (or sandbox)
- **Sharing ID**: Auto-injected into query params by `_inject_sharing_id()` (for `get()` and `post()` only)
- **Error handling**: Parses JSON error bodies into `GandiAPIError` with cause/message/object
- **Response handling**: JSON parsed automatically, 204 returns `{}`, non-JSON returns raw text

### Certificate Commands: Implemented vs Missing
| Command | Status | API Endpoint |
|---------|--------|--------------|
| `cert list` | ✅ Implemented | `GET /certificate/issued-certs` |
| `cert info` | ✅ Implemented | `GET /certificate/issued-certs/{id}` |
| `cert create` | ❌ Missing | `POST /certificate/issued-certs` |
| `cert update` | ❌ Missing | `PATCH /certificate/issued-certs/{id}` |
| `cert revoke`/`delete` | ❌ Missing | `DELETE /certificate/issued-certs/{id}` |
| `cert dcv` | ❌ Missing | `GET /certificate/issued-certs/{id}/dcv` |
| `cert packages` | ❌ Missing | `GET /certificate/packages` |
| `cert package-info` | ❌ Missing | `GET /certificate/packages/{name}` |

### Test Patterns
1. **Runner**: `CliRunner()` from `typer.testing`
2. **App wrapping**: Tests create a local `typer.Typer()` and add the sub-app (avoids needing full main app state)
3. **Client mocking**: `unittest.mock.patch("gandi_cli.commands.certificate._get_client")` replaces the helper, returning a real `GandiClient(token="test-token")` that makes real HTTP calls
4. **HTTP mocking**: `pytest-httpx`'s `httpx_mock` fixture intercepts those HTTP calls with `add_response(json=fixture_data)`
5. **Fixtures**: JSON files in `tests/fixtures/`, loaded via `load_fixture()` helper
6. **Assertions**: Check `exit_code == 0`, check expected strings appear in `result.stdout`, verify request URLs/params via `httpx_mock.get_request()`
7. **Test organization**: Tests grouped in classes (`TestCertList`, `TestCertInfo`) with descriptive method names

### Output Formatting Conventions
- **Lists** (table format): Define `columns = [("key", "Header Label"), ...]`, call `output(data, fmt=state.output_format, columns=columns, title="Title")`
- **Details** (single record): Define `fields = [("key", "Label"), ...]`, call `output(data, fmt=state.output_format, detail_fields=fields)`
- **Nested data**: Must be flattened before passing to output (e.g., `data["dates.ends_at"] = dates.get("ends_at")[:10]`)
- **Lists in values**: Joined with `", "` (e.g., altnames)
- **Success messages** for mutations: Simple `typer.echo("message")`
- **Error messages**: `typer.echo(f"Error: {e}", err=True)` + `raise typer.Exit(1)`
- **Three formats**: `table` (Rich tables), `json` (Rich JSON), `plain` (tab-separated/key-value)
