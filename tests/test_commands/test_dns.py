"""Tests for LiveDNS commands."""

from unittest.mock import patch

import typer
from typer.testing import CliRunner
from pytest_httpx import HTTPXMock

from gandi_cli.client import GandiClient
from gandi_cli.commands.dns import dns_app
from tests.conftest import load_fixture

runner = CliRunner()

BASE_URL = "https://api.gandi.net/v5"

# Wrap dns_app in a top-level app so CliRunner can invoke it
app = typer.Typer()
app.add_typer(dns_app, name="dns")


def _patch_get_client(client: GandiClient):
    """Return a context manager that patches _get_client to return the given client."""
    return patch("gandi_cli.commands.dns._get_client", return_value=client)


def _patch_state(output_format: str = "plain"):
    """Patch the state object in gandi_cli.main so lazy imports pick it up."""
    from gandi_cli.main import State

    mock_state = State()
    mock_state.token = "test-token"
    mock_state.output_format = output_format
    return patch("gandi_cli.main.state", mock_state)


class TestDnsList:
    def test_dns_list(self, httpx_mock: HTTPXMock):
        records = load_fixture("dns_records.json")
        httpx_mock.add_response(
            url=f"{BASE_URL}/livedns/domains/example.com/records",
            json=records,
        )
        client = GandiClient(token="test-token")
        with _patch_get_client(client), _patch_state():
            result = runner.invoke(app, ["dns", "list", "example.com"])
        client.close()
        assert result.exit_code == 0
        assert "203.0.113.1" in result.output
        assert "www" in result.output
        assert "CNAME" in result.output
        assert "MX" in result.output

    def test_dns_list_filter_type(self, httpx_mock: HTTPXMock):
        records = load_fixture("dns_records.json")
        httpx_mock.add_response(
            url=f"{BASE_URL}/livedns/domains/example.com/records",
            json=records,
        )
        client = GandiClient(token="test-token")
        with _patch_get_client(client), _patch_state():
            result = runner.invoke(app, ["dns", "list", "example.com", "--type", "A"])
        client.close()
        assert result.exit_code == 0
        assert "203.0.113.1" in result.output
        assert "203.0.113.2" in result.output
        # CNAME and MX should be filtered out
        assert "CNAME" not in result.output
        assert "MX" not in result.output


class TestDnsGet:
    def test_dns_get(self, httpx_mock: HTTPXMock):
        record = {
            "rrset_name": "www",
            "rrset_type": "CNAME",
            "rrset_ttl": 10800,
            "rrset_values": ["example.com."],
        }
        httpx_mock.add_response(
            url=f"{BASE_URL}/livedns/domains/example.com/records/www/CNAME",
            json=record,
        )
        client = GandiClient(token="test-token")
        with _patch_get_client(client), _patch_state():
            result = runner.invoke(app, ["dns", "get", "example.com", "www", "CNAME"])
        client.close()
        assert result.exit_code == 0
        assert "www" in result.output
        assert "CNAME" in result.output
        assert "example.com." in result.output


class TestDnsCreate:
    def test_dns_create(self, httpx_mock: HTTPXMock):
        httpx_mock.add_response(
            url=f"{BASE_URL}/livedns/domains/example.com/records",
            method="POST",
            json={"message": "DNS Record Created"},
            status_code=201,
        )
        client = GandiClient(token="test-token")
        with _patch_get_client(client), _patch_state():
            result = runner.invoke(
                app,
                ["dns", "create", "example.com", "test", "A", "203.0.113.10"],
            )
        client.close()
        assert result.exit_code == 0
        assert "Created A record 'test' for example.com" in result.output


class TestDnsUpdate:
    def test_dns_update(self, httpx_mock: HTTPXMock):
        httpx_mock.add_response(
            url=f"{BASE_URL}/livedns/domains/example.com/records/test/A",
            method="PUT",
            json={"message": "DNS Record Updated"},
        )
        client = GandiClient(token="test-token")
        with _patch_get_client(client), _patch_state():
            result = runner.invoke(
                app,
                [
                    "dns", "update", "example.com", "test", "A",
                    "--value", "203.0.113.20",
                ],
            )
        client.close()
        assert result.exit_code == 0
        assert "Updated A record 'test' for example.com" in result.output


class TestDnsDelete:
    def test_dns_delete_with_force(self, httpx_mock: HTTPXMock):
        httpx_mock.add_response(
            url=f"{BASE_URL}/livedns/domains/example.com/records/test/A",
            method="DELETE",
            status_code=204,
        )
        client = GandiClient(token="test-token")
        with _patch_get_client(client), _patch_state():
            result = runner.invoke(
                app,
                ["dns", "delete", "example.com", "test", "A", "--force"],
            )
        client.close()
        assert result.exit_code == 0
        assert "Deleted A record 'test' from example.com" in result.output


class TestDnsExport:
    def test_dns_export(self, httpx_mock: HTTPXMock):
        zone_text = "@ 10800 IN A 203.0.113.1\nwww 10800 IN CNAME example.com."
        httpx_mock.add_response(
            url=f"{BASE_URL}/livedns/domains/example.com/records",
            text=zone_text,
            headers={"content-type": "text/plain"},
        )
        client = GandiClient(token="test-token")
        with _patch_get_client(client), _patch_state():
            result = runner.invoke(app, ["dns", "export", "example.com"])
        client.close()
        assert result.exit_code == 0
        assert "@ 10800 IN A 203.0.113.1" in result.output
        assert "www 10800 IN CNAME example.com." in result.output
