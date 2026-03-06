"""Tests for email commands."""

import json
from pathlib import Path
from unittest.mock import patch

import typer
from typer.testing import CliRunner
from pytest_httpx import HTTPXMock

from gandi_cli.client import GandiClient
from gandi_cli.commands.email import email_app

runner = CliRunner()

# Wrap email_app in a top-level app so CliRunner can invoke it
app = typer.Typer()
app.add_typer(email_app, name="email")

FIXTURES_DIR = Path(__file__).parent.parent / "fixtures"


def load_fixture(name: str):
    return json.loads((FIXTURES_DIR / name).read_text())


class TestForwardList:
    """Tests for the forward list command."""

    def test_forward_list(self, httpx_mock: HTTPXMock):
        fixture = load_fixture("email_forwards.json")
        httpx_mock.add_response(json=fixture)

        with patch("gandi_cli.commands.email._get_client") as mock_client:
            mock_client.return_value = GandiClient(token="test-token")
            result = runner.invoke(app, ["email", "forward", "list", "example.com"])

        assert result.exit_code == 0
        assert "info" in result.stdout
        assert "support" in result.stdout
        assert "john@gmail.com" in result.stdout
        assert "team@company.com" in result.stdout


class TestForwardCreate:
    """Tests for the forward create command."""

    def test_forward_create(self, httpx_mock: HTTPXMock):
        httpx_mock.add_response(status_code=201, json={"message": "Created"})

        with patch("gandi_cli.commands.email._get_client") as mock_client:
            mock_client.return_value = GandiClient(token="test-token")
            result = runner.invoke(
                app,
                ["email", "forward", "create", "example.com", "info", "john@gmail.com"],
            )

        assert result.exit_code == 0
        assert "Created forward" in result.stdout
        assert "info@example.com" in result.stdout
        assert "john@gmail.com" in result.stdout

        request = httpx_mock.get_request()
        body = json.loads(request.content)
        assert body["source"] == "info"
        assert body["destinations"] == ["john@gmail.com"]


class TestForwardDelete:
    """Tests for the forward delete command."""

    def test_forward_delete_with_force(self, httpx_mock: HTTPXMock):
        httpx_mock.add_response(status_code=204)

        with patch("gandi_cli.commands.email._get_client") as mock_client:
            mock_client.return_value = GandiClient(token="test-token")
            result = runner.invoke(
                app,
                ["email", "forward", "delete", "example.com", "info", "--force"],
            )

        assert result.exit_code == 0
        assert "Deleted forward" in result.stdout
        assert "info@example.com" in result.stdout

        request = httpx_mock.get_request()
        assert "/email/forwards/example.com/info" in str(request.url)


class TestMailboxList:
    """Tests for the mailbox list command."""

    def test_mailbox_list(self, httpx_mock: HTTPXMock):
        fixture = load_fixture("mailboxes.json")
        httpx_mock.add_response(json=fixture)

        with patch("gandi_cli.commands.email._get_client") as mock_client:
            mock_client.return_value = GandiClient(token="test-token")
            result = runner.invoke(app, ["email", "mailbox", "list", "example.com"])

        assert result.exit_code == 0
        assert "mb-001" in result.stdout
        assert "mb-002" in result.stdout
        assert "admin@example.com" in result.stdout
        assert "standard" in result.stdout
        assert "premium" in result.stdout


class TestMailboxInfo:
    """Tests for the mailbox info command."""

    def test_mailbox_info(self, httpx_mock: HTTPXMock):
        fixture = load_fixture("mailboxes.json")[1]  # Use the premium mailbox
        httpx_mock.add_response(json=fixture)

        with patch("gandi_cli.commands.email._get_client") as mock_client:
            mock_client.return_value = GandiClient(token="test-token")
            result = runner.invoke(
                app, ["email", "mailbox", "info", "example.com", "mb-002"]
            )

        assert result.exit_code == 0
        assert "mb-002" in result.stdout
        assert "info@example.com" in result.stdout
        assert "premium" in result.stdout
        assert "contact@example.com" in result.stdout

        request = httpx_mock.get_request()
        assert "/email/mailboxes/example.com/mb-002" in str(request.url)
