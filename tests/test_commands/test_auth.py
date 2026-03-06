"""Tests for auth commands."""

from unittest.mock import MagicMock, patch

import typer
from typer.testing import CliRunner

from gandi_cli.commands.auth import auth_app
from gandi_cli.config import AuthConfig, DefaultsConfig, GandiConfig

runner = CliRunner()

# Wrap auth_app in a top-level app so CliRunner can invoke it
app = typer.Typer()
app.add_typer(auth_app, name="auth")


def _make_config(pat: str = "", sharing_id: str = "", output: str = "table") -> GandiConfig:
    return GandiConfig(
        auth=AuthConfig(pat=pat),
        defaults=DefaultsConfig(sharing_id=sharing_id, output=output),
    )


class TestLogin:
    """Tests for the login command."""

    @patch("gandi_cli.commands.auth.save_config")
    @patch("gandi_cli.commands.auth.load_config")
    def test_login_with_token_option(self, mock_load, mock_save):
        mock_load.return_value = _make_config()
        result = runner.invoke(app, ["auth", "login", "--token", "my-secret-token"])
        assert result.exit_code == 0
        assert "Token saved" in result.output
        saved_config = mock_save.call_args[0][0]
        assert saved_config.auth.pat == "my-secret-token"

    @patch("gandi_cli.commands.auth.save_config")
    @patch("gandi_cli.commands.auth.load_config")
    def test_login_with_short_flag(self, mock_load, mock_save):
        mock_load.return_value = _make_config()
        result = runner.invoke(app, ["auth", "login", "-t", "short-flag-token"])
        assert result.exit_code == 0
        assert "Token saved" in result.output
        saved_config = mock_save.call_args[0][0]
        assert saved_config.auth.pat == "short-flag-token"

    @patch("gandi_cli.commands.auth.save_config")
    @patch("gandi_cli.commands.auth.load_config")
    def test_login_prompts_when_no_token(self, mock_load, mock_save):
        mock_load.return_value = _make_config()
        result = runner.invoke(app, ["auth", "login"], input="prompted-token\n")
        assert result.exit_code == 0
        assert "Token saved" in result.output
        saved_config = mock_save.call_args[0][0]
        assert saved_config.auth.pat == "prompted-token"

    @patch("gandi_cli.commands.auth.save_config")
    @patch("gandi_cli.commands.auth.load_config")
    def test_login_empty_token_fails(self, mock_load, mock_save):
        mock_load.return_value = _make_config()
        result = runner.invoke(app, ["auth", "login", "--token", ""])
        assert result.exit_code == 1
        assert "Error" in result.output
        mock_save.assert_not_called()


class TestLogout:
    """Tests for the logout command."""

    @patch("gandi_cli.commands.auth.save_config")
    @patch("gandi_cli.commands.auth.load_config")
    def test_logout_removes_token(self, mock_load, mock_save):
        mock_load.return_value = _make_config(pat="existing-token")
        result = runner.invoke(app, ["auth", "logout"])
        assert result.exit_code == 0
        assert "Token removed" in result.output
        saved_config = mock_save.call_args[0][0]
        assert saved_config.auth.pat == ""

    @patch("gandi_cli.commands.auth.save_config")
    @patch("gandi_cli.commands.auth.load_config")
    def test_logout_no_token_configured(self, mock_load, mock_save):
        mock_load.return_value = _make_config(pat="")
        result = runner.invoke(app, ["auth", "logout"])
        assert result.exit_code == 0
        assert "No token configured" in result.output
        mock_save.assert_not_called()


class TestStatus:
    """Tests for the status command."""

    @patch("gandi_cli.commands.auth.load_config")
    def test_status_shows_token_from_config(self, mock_load):
        mock_load.return_value = _make_config(pat="abcdefghijklmnop", sharing_id="org-123")
        result = runner.invoke(app, ["auth", "status"], env={"GANDI_PAT": ""})
        assert result.exit_code == 0
        assert "abcdefgh" in result.output  # first 8 chars visible
        assert "mnop" in result.output  # last 4 chars visible
        assert "config" in result.output
        assert "org-123" in result.output

    @patch("gandi_cli.commands.auth.load_config")
    def test_status_shows_token_from_env(self, mock_load):
        mock_load.return_value = _make_config(pat="")
        result = runner.invoke(
            app, ["auth", "status"], env={"GANDI_PAT": "env-token-abcdefghijklm"}
        )
        assert result.exit_code == 0
        assert "env:GANDI_PAT" in result.output

    @patch("gandi_cli.commands.auth.load_config")
    def test_status_no_token(self, mock_load):
        mock_load.return_value = _make_config()
        result = runner.invoke(app, ["auth", "status"], env={"GANDI_PAT": ""})
        assert result.exit_code == 0
        assert "No token configured" in result.output

    @patch("gandi_cli.commands.auth.load_config")
    def test_status_shows_output_format(self, mock_load):
        mock_load.return_value = _make_config(output="json")
        result = runner.invoke(app, ["auth", "status"], env={"GANDI_PAT": ""})
        assert result.exit_code == 0
        assert "json" in result.output

    @patch("gandi_cli.commands.auth.load_config")
    def test_status_short_token_masked(self, mock_load):
        mock_load.return_value = _make_config(pat="short")
        result = runner.invoke(app, ["auth", "status"], env={"GANDI_PAT": ""})
        assert result.exit_code == 0
        assert "***" in result.output


class TestSetOrg:
    """Tests for the set-org command."""

    @patch("gandi_cli.commands.auth.save_config")
    @patch("gandi_cli.commands.auth.load_config")
    def test_set_org_saves_sharing_id(self, mock_load, mock_save):
        mock_load.return_value = _make_config()
        result = runner.invoke(app, ["auth", "set-org", "my-org-id-456"])
        assert result.exit_code == 0
        assert "my-org-id-456" in result.output
        saved_config = mock_save.call_args[0][0]
        assert saved_config.defaults.sharing_id == "my-org-id-456"

    @patch("gandi_cli.commands.auth.save_config")
    @patch("gandi_cli.commands.auth.load_config")
    def test_set_org_overwrites_existing(self, mock_load, mock_save):
        mock_load.return_value = _make_config(sharing_id="old-org")
        result = runner.invoke(app, ["auth", "set-org", "new-org"])
        assert result.exit_code == 0
        saved_config = mock_save.call_args[0][0]
        assert saved_config.defaults.sharing_id == "new-org"

    def test_set_org_requires_argument(self):
        result = runner.invoke(app, ["auth", "set-org"])
        assert result.exit_code != 0
