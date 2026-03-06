"""Tests for certificate commands."""

import json
from pathlib import Path
from unittest.mock import patch

import typer
from typer.testing import CliRunner
from pytest_httpx import HTTPXMock

from gandi_cli.client import GandiClient
from gandi_cli.commands.certificate import cert_app

runner = CliRunner()

# Wrap cert_app in a top-level app so CliRunner can invoke it
app = typer.Typer()
app.add_typer(cert_app, name="cert")

FIXTURES_DIR = Path(__file__).parent.parent / "fixtures"


def load_fixture(name: str):
    return json.loads((FIXTURES_DIR / name).read_text())


class TestCertList:
    """Tests for the certificate list command."""

    def test_cert_list(self, httpx_mock: HTTPXMock):
        fixture = load_fixture("certificates.json")
        httpx_mock.add_response(json=fixture)

        with patch("gandi_cli.commands.certificate._get_client") as mock_client:
            mock_client.return_value = GandiClient(token="test-token")
            result = runner.invoke(app, ["cert", "list"])

        assert result.exit_code == 0
        assert "example.com" in result.stdout
        assert "shop.example.com" in result.stdout
        assert "cert-001" in result.stdout
        assert "cert-002" in result.stdout

    def test_cert_list_shows_status(self, httpx_mock: HTTPXMock):
        fixture = load_fixture("certificates.json")
        httpx_mock.add_response(json=fixture)

        with patch("gandi_cli.commands.certificate._get_client") as mock_client:
            mock_client.return_value = GandiClient(token="test-token")
            result = runner.invoke(app, ["cert", "list"])

        assert result.exit_code == 0
        assert "valid" in result.stdout
        assert "expired" in result.stdout

    def test_cert_list_shows_expiry_date(self, httpx_mock: HTTPXMock):
        fixture = load_fixture("certificates.json")
        httpx_mock.add_response(json=fixture)

        with patch("gandi_cli.commands.certificate._get_client") as mock_client:
            mock_client.return_value = GandiClient(token="test-token")
            result = runner.invoke(app, ["cert", "list"])

        assert result.exit_code == 0
        assert "2025-01-01" in result.stdout
        assert "2024-06-15" in result.stdout

    def test_cert_list_shows_package(self, httpx_mock: HTTPXMock):
        fixture = load_fixture("certificates.json")
        httpx_mock.add_response(json=fixture)

        with patch("gandi_cli.commands.certificate._get_client") as mock_client:
            mock_client.return_value = GandiClient(token="test-token")
            result = runner.invoke(app, ["cert", "list"])

        assert result.exit_code == 0
        assert "std_dv_1y" in result.stdout

    def test_cert_list_with_cn_filter(self, httpx_mock: HTTPXMock):
        fixture = [load_fixture("certificates.json")[0]]
        httpx_mock.add_response(json=fixture)

        with patch("gandi_cli.commands.certificate._get_client") as mock_client:
            mock_client.return_value = GandiClient(token="test-token")
            result = runner.invoke(
                app, ["cert", "list", "--cn", "example.com"]
            )

        assert result.exit_code == 0
        assert "example.com" in result.stdout

        # Verify the cn param was sent
        request = httpx_mock.get_request()
        assert "cn=example.com" in str(request.url)

    def test_cert_list_with_status_filter(self, httpx_mock: HTTPXMock):
        fixture = [load_fixture("certificates.json")[0]]
        httpx_mock.add_response(json=fixture)

        with patch("gandi_cli.commands.certificate._get_client") as mock_client:
            mock_client.return_value = GandiClient(token="test-token")
            result = runner.invoke(
                app, ["cert", "list", "--status", "valid"]
            )

        assert result.exit_code == 0

        # Verify the status param was sent
        request = httpx_mock.get_request()
        assert "status=valid" in str(request.url)


class TestCertInfo:
    """Tests for the certificate info command."""

    def test_cert_info(self, httpx_mock: HTTPXMock):
        fixture = load_fixture("certificate_detail.json")
        httpx_mock.add_response(json=fixture)

        with patch("gandi_cli.commands.certificate._get_client") as mock_client:
            mock_client.return_value = GandiClient(token="test-token")
            result = runner.invoke(app, ["cert", "info", "cert-001"])

        assert result.exit_code == 0
        assert "cert-001" in result.stdout
        assert "example.com" in result.stdout
        assert "valid" in result.stdout

    def test_cert_info_shows_altnames(self, httpx_mock: HTTPXMock):
        fixture = load_fixture("certificate_detail.json")
        httpx_mock.add_response(json=fixture)

        with patch("gandi_cli.commands.certificate._get_client") as mock_client:
            mock_client.return_value = GandiClient(token="test-token")
            result = runner.invoke(app, ["cert", "info", "cert-001"])

        assert result.exit_code == 0
        assert "www.example.com" in result.stdout
        assert "mail.example.com" in result.stdout

    def test_cert_info_shows_dates(self, httpx_mock: HTTPXMock):
        fixture = load_fixture("certificate_detail.json")
        httpx_mock.add_response(json=fixture)

        with patch("gandi_cli.commands.certificate._get_client") as mock_client:
            mock_client.return_value = GandiClient(token="test-token")
            result = runner.invoke(app, ["cert", "info", "cert-001"])

        assert result.exit_code == 0
        assert "2024-01-01" in result.stdout
        assert "2025-01-01" in result.stdout

    def test_cert_info_shows_package(self, httpx_mock: HTTPXMock):
        fixture = load_fixture("certificate_detail.json")
        httpx_mock.add_response(json=fixture)

        with patch("gandi_cli.commands.certificate._get_client") as mock_client:
            mock_client.return_value = GandiClient(token="test-token")
            result = runner.invoke(app, ["cert", "info", "cert-001"])

        assert result.exit_code == 0
        assert "std_dv_1y" in result.stdout

    def test_cert_info_requests_correct_url(self, httpx_mock: HTTPXMock):
        fixture = load_fixture("certificate_detail.json")
        httpx_mock.add_response(json=fixture)

        with patch("gandi_cli.commands.certificate._get_client") as mock_client:
            mock_client.return_value = GandiClient(token="test-token")
            result = runner.invoke(app, ["cert", "info", "cert-001"])

        assert result.exit_code == 0
        request = httpx_mock.get_request()
        assert "/certificate/issued-certs/cert-001" in str(request.url)
