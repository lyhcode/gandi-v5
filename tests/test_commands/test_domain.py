"""Tests for domain commands."""

import json
from pathlib import Path
from unittest.mock import patch

import typer
from typer.testing import CliRunner
from pytest_httpx import HTTPXMock

from gandi_cli.client import GandiClient
from gandi_cli.commands.domain import domain_app

runner = CliRunner()

# Wrap domain_app in a top-level app so CliRunner can invoke it
app = typer.Typer()
app.add_typer(domain_app, name="domain")

FIXTURES_DIR = Path(__file__).parent.parent / "fixtures"


def load_fixture(name: str):
    return json.loads((FIXTURES_DIR / name).read_text())


class TestDomainList:
    """Tests for the domain list command."""

    def test_domain_list(self, httpx_mock: HTTPXMock):
        fixture = load_fixture("domains_list.json")
        httpx_mock.add_response(json=fixture)

        with patch("gandi_cli.commands.domain._get_client") as mock_client:
            mock_client.return_value = GandiClient(token="test-token")
            result = runner.invoke(app, ["domain", "list"])

        assert result.exit_code == 0
        assert "example.com" in result.stdout
        assert "example.net" in result.stdout

    def test_domain_list_with_fqdn_filter(self, httpx_mock: HTTPXMock):
        fixture = [load_fixture("domains_list.json")[0]]
        httpx_mock.add_response(json=fixture)

        with patch("gandi_cli.commands.domain._get_client") as mock_client:
            mock_client.return_value = GandiClient(token="test-token")
            result = runner.invoke(
                app, ["domain", "list", "--fqdn", "example.com"]
            )

        assert result.exit_code == 0
        assert "example.com" in result.stdout

        # Verify the fqdn param was sent
        request = httpx_mock.get_request()
        assert "fqdn=example.com" in str(request.url)

    def test_domain_list_shows_expiry_date(self, httpx_mock: HTTPXMock):
        fixture = load_fixture("domains_list.json")
        httpx_mock.add_response(json=fixture)

        with patch("gandi_cli.commands.domain._get_client") as mock_client:
            mock_client.return_value = GandiClient(token="test-token")
            result = runner.invoke(app, ["domain", "list"])

        assert result.exit_code == 0
        assert "2025-12-31" in result.stdout

    def test_domain_list_shows_autorenew(self, httpx_mock: HTTPXMock):
        fixture = load_fixture("domains_list.json")
        httpx_mock.add_response(json=fixture)

        with patch("gandi_cli.commands.domain._get_client") as mock_client:
            mock_client.return_value = GandiClient(token="test-token")
            result = runner.invoke(app, ["domain", "list"])

        assert result.exit_code == 0
        assert "Yes" in result.stdout
        assert "No" in result.stdout


class TestDomainInfo:
    """Tests for the domain info command."""

    def test_domain_info(self, httpx_mock: HTTPXMock):
        fixture = load_fixture("domain_detail.json")
        httpx_mock.add_response(json=fixture)

        with patch("gandi_cli.commands.domain._get_client") as mock_client:
            mock_client.return_value = GandiClient(token="test-token")
            result = runner.invoke(app, ["domain", "info", "example.com"])

        assert result.exit_code == 0
        assert "example.com" in result.stdout
        assert "John Doe" in result.stdout
        assert "My Org" in result.stdout

    def test_domain_info_shows_nameservers(self, httpx_mock: HTTPXMock):
        fixture = load_fixture("domain_detail.json")
        httpx_mock.add_response(json=fixture)

        with patch("gandi_cli.commands.domain._get_client") as mock_client:
            mock_client.return_value = GandiClient(token="test-token")
            result = runner.invoke(app, ["domain", "info", "example.com"])

        assert result.exit_code == 0
        assert "ns1.gandi.net" in result.stdout
        assert "ns2.gandi.net" in result.stdout

    def test_domain_info_shows_dates(self, httpx_mock: HTTPXMock):
        fixture = load_fixture("domain_detail.json")
        httpx_mock.add_response(json=fixture)

        with patch("gandi_cli.commands.domain._get_client") as mock_client:
            mock_client.return_value = GandiClient(token="test-token")
            result = runner.invoke(app, ["domain", "info", "example.com"])

        assert result.exit_code == 0
        assert "2020-01-15" in result.stdout
        assert "2025-12-31" in result.stdout

    def test_domain_info_shows_tags(self, httpx_mock: HTTPXMock):
        fixture = load_fixture("domain_detail.json")
        httpx_mock.add_response(json=fixture)

        with patch("gandi_cli.commands.domain._get_client") as mock_client:
            mock_client.return_value = GandiClient(token="test-token")
            result = runner.invoke(app, ["domain", "info", "example.com"])

        assert result.exit_code == 0
        assert "production" in result.stdout


class TestDomainCheck:
    """Tests for the domain check command."""

    def test_domain_check(self, httpx_mock: HTTPXMock):
        fixture = load_fixture("domain_check.json")
        httpx_mock.add_response(json=fixture)

        with patch("gandi_cli.commands.domain._get_client") as mock_client:
            mock_client.return_value = GandiClient(token="test-token")
            result = runner.invoke(app, ["domain", "check", "example.com"])

        assert result.exit_code == 0
        assert "available" in result.stdout
        assert "12.99" in result.stdout
        assert "USD" in result.stdout

    def test_domain_check_with_currency(self, httpx_mock: HTTPXMock):
        fixture = load_fixture("domain_check.json")
        httpx_mock.add_response(json=fixture)

        with patch("gandi_cli.commands.domain._get_client") as mock_client:
            mock_client.return_value = GandiClient(token="test-token")
            result = runner.invoke(
                app,
                ["domain", "check", "example.com", "--currency", "EUR"],
            )

        assert result.exit_code == 0
        # Verify currency param was sent
        request = httpx_mock.get_request()
        assert "currency=EUR" in str(request.url)

    def test_domain_check_no_products(self, httpx_mock: HTTPXMock):
        httpx_mock.add_response(
            json={"currency": "USD", "products": []}
        )

        with patch("gandi_cli.commands.domain._get_client") as mock_client:
            mock_client.return_value = GandiClient(token="test-token")
            result = runner.invoke(app, ["domain", "check", "example.com"])

        assert result.exit_code == 0
        assert "No results" in result.stdout
