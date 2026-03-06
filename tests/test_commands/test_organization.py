"""Tests for organization commands."""

import json
from unittest.mock import patch, MagicMock

import typer
from typer.testing import CliRunner

from gandi_cli.commands.organization import org_app
from gandi_cli.client import GandiClient
from tests.conftest import load_fixture

runner = CliRunner()

# Wrap org_app in a top-level app so CliRunner can invoke it
app = typer.Typer()
app.add_typer(org_app, name="org")


def _mock_client(httpx_mock, token="test-token-123", sharing_id="test-org-id"):
    """Create a real GandiClient wired to httpx_mock and patch _get_client."""
    client = GandiClient(token=token, sharing_id=sharing_id)
    patcher = patch(
        "gandi_cli.commands.organization._get_client", return_value=client
    )
    patcher.start()
    return patcher


class TestOrgList:
    """Tests for the org list command."""

    def test_org_list(self, httpx_mock):
        fixture = load_fixture("organizations.json")
        httpx_mock.add_response(
            url="https://api.gandi.net/v5/organization/organizations?page=1&per_page=25&sharing_id=test-org-id",
            json=fixture,
        )
        patcher = _mock_client(httpx_mock)
        try:
            result = runner.invoke(app, ["org", "list"])
            assert result.exit_code == 0
            assert "org-001" in result.output
            assert "My Organization" in result.output
            assert "org-002" in result.output
            assert "Company Inc" in result.output
        finally:
            patcher.stop()

    def test_org_list_with_name_filter(self, httpx_mock):
        fixture = [load_fixture("organizations.json")[0]]
        httpx_mock.add_response(
            url="https://api.gandi.net/v5/organization/organizations?page=1&per_page=25&name=My+Organization&sharing_id=test-org-id",
            json=fixture,
        )
        patcher = _mock_client(httpx_mock)
        try:
            result = runner.invoke(
                    app, ["org", "list", "--name", "My Organization"]
                )
            assert result.exit_code == 0
            assert "My Organization" in result.output
        finally:
            patcher.stop()


class TestOrgInfo:
    """Tests for the org info command."""

    def test_org_info(self, httpx_mock):
        fixture = {
            "id": "org-001",
            "name": "My Organization",
            "type": "individual",
            "orgname": "myorg",
            "email": "admin@example.com",
            "vat_number": "",
            "corporate": False,
        }
        httpx_mock.add_response(
            url="https://api.gandi.net/v5/organization/organizations/org-001?sharing_id=test-org-id",
            json=fixture,
        )
        patcher = _mock_client(httpx_mock)
        try:
            result = runner.invoke(app, ["org", "info", "org-001"])
            assert result.exit_code == 0
            assert "org-001" in result.output
            assert "My Organization" in result.output
            assert "admin@example.com" in result.output
        finally:
            patcher.stop()


class TestWhoami:
    """Tests for the whoami command."""

    def test_whoami(self, httpx_mock):
        fixture = {
            "username": "johndoe",
            "email": "john@example.com",
            "firstname": "John",
            "lastname": "Doe",
            "id": "user-abc-123",
            "lang": "en",
        }
        httpx_mock.add_response(
            url="https://api.gandi.net/v5/organization/user-info?sharing_id=test-org-id",
            json=fixture,
        )
        patcher = _mock_client(httpx_mock)
        try:
            result = runner.invoke(app, ["org", "whoami"])
            assert result.exit_code == 0
            assert "johndoe" in result.output
            assert "john@example.com" in result.output
            assert "John" in result.output
            assert "Doe" in result.output
            assert "user-abc-123" in result.output
        finally:
            patcher.stop()
