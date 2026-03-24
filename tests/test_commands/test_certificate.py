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


class TestCertReissue:
    """Tests for the certificate reissue command."""

    def test_cert_reissue(self, httpx_mock: HTTPXMock, tmp_path):
        fixture = load_fixture("reissue_response.json")
        httpx_mock.add_response(json=fixture)
        csr_file = tmp_path / "test.csr"
        csr_file.write_text("-----BEGIN CERTIFICATE REQUEST-----\ntest\n-----END CERTIFICATE REQUEST-----\n")

        with patch("gandi_cli.commands.certificate._get_client") as mock_client:
            mock_client.return_value = GandiClient(token="test-token")
            result = runner.invoke(app, ["cert", "reissue", "cert-001", "--csr", str(csr_file)])

        assert result.exit_code == 0
        assert "reissue submitted" in result.stdout.lower()

    def test_cert_reissue_sends_correct_url(self, httpx_mock: HTTPXMock, tmp_path):
        fixture = load_fixture("reissue_response.json")
        httpx_mock.add_response(json=fixture)
        csr_file = tmp_path / "test.csr"
        csr_file.write_text("-----BEGIN CERTIFICATE REQUEST-----\ntest\n-----END CERTIFICATE REQUEST-----\n")

        with patch("gandi_cli.commands.certificate._get_client") as mock_client:
            mock_client.return_value = GandiClient(token="test-token")
            result = runner.invoke(app, ["cert", "reissue", "cert-001", "--csr", str(csr_file)])

        assert result.exit_code == 0
        request = httpx_mock.get_request()
        assert request.method == "POST"
        assert "/certificate/issued-certs/cert-001" in str(request.url)

    def test_cert_reissue_sends_csr_in_body(self, httpx_mock: HTTPXMock, tmp_path):
        fixture = load_fixture("reissue_response.json")
        httpx_mock.add_response(json=fixture)
        csr_file = tmp_path / "test.csr"
        csr_text = "-----BEGIN CERTIFICATE REQUEST-----\ntest\n-----END CERTIFICATE REQUEST-----\n"
        csr_file.write_text(csr_text)

        with patch("gandi_cli.commands.certificate._get_client") as mock_client:
            mock_client.return_value = GandiClient(token="test-token")
            result = runner.invoke(app, ["cert", "reissue", "cert-001", "--csr", str(csr_file)])

        assert result.exit_code == 0
        request = httpx_mock.get_request()
        body = json.loads(request.content)
        assert "csr" in body
        assert "BEGIN CERTIFICATE REQUEST" in body["csr"]

    def test_cert_reissue_with_dcv_method(self, httpx_mock: HTTPXMock, tmp_path):
        fixture = load_fixture("reissue_response.json")
        httpx_mock.add_response(json=fixture)
        csr_file = tmp_path / "test.csr"
        csr_file.write_text("-----BEGIN CERTIFICATE REQUEST-----\ntest\n-----END CERTIFICATE REQUEST-----\n")

        with patch("gandi_cli.commands.certificate._get_client") as mock_client:
            mock_client.return_value = GandiClient(token="test-token")
            result = runner.invoke(app, ["cert", "reissue", "cert-001", "--csr", str(csr_file), "--dcv-method", "dns"])

        assert result.exit_code == 0
        request = httpx_mock.get_request()
        body = json.loads(request.content)
        assert body["dcv_method"] == "dns"

    def test_cert_reissue_with_duration(self, httpx_mock: HTTPXMock, tmp_path):
        fixture = load_fixture("reissue_response.json")
        httpx_mock.add_response(json=fixture)
        csr_file = tmp_path / "test.csr"
        csr_file.write_text("-----BEGIN CERTIFICATE REQUEST-----\ntest\n-----END CERTIFICATE REQUEST-----\n")

        with patch("gandi_cli.commands.certificate._get_client") as mock_client:
            mock_client.return_value = GandiClient(token="test-token")
            result = runner.invoke(app, ["cert", "reissue", "cert-001", "--csr", str(csr_file), "--duration", "2"])

        assert result.exit_code == 0
        request = httpx_mock.get_request()
        body = json.loads(request.content)
        assert body["duration"] == 2

    def test_cert_reissue_dry_run(self, httpx_mock: HTTPXMock, tmp_path):
        httpx_mock.add_response(json={})
        csr_file = tmp_path / "test.csr"
        csr_file.write_text("-----BEGIN CERTIFICATE REQUEST-----\ntest\n-----END CERTIFICATE REQUEST-----\n")

        with patch("gandi_cli.commands.certificate._get_client") as mock_client:
            mock_client.return_value = GandiClient(token="test-token")
            result = runner.invoke(app, ["cert", "reissue", "cert-001", "--csr", str(csr_file), "--dry-run"])

        assert result.exit_code == 0
        assert "dry run" in result.stdout.lower()
        request = httpx_mock.get_request()
        assert request.headers.get("dry-run") == "1"

    def test_cert_reissue_missing_csr_file(self):
        with patch("gandi_cli.commands.certificate._get_client") as mock_client:
            mock_client.return_value = GandiClient(token="test-token")
            result = runner.invoke(app, ["cert", "reissue", "cert-001", "--csr", "/nonexistent/file.csr"])

        assert result.exit_code == 1


class TestCertDcvInfo:
    """Tests for the certificate dcv-info command."""

    def test_cert_dcv_info(self, httpx_mock: HTTPXMock):
        fixture = load_fixture("dcv_params.json")
        httpx_mock.add_response(json=fixture)

        with patch("gandi_cli.commands.certificate._get_client") as mock_client:
            mock_client.return_value = GandiClient(token="test-token")
            result = runner.invoke(app, ["cert", "dcv-info", "cert-001"])

        assert result.exit_code == 0
        assert "example.com" in result.stdout

    def test_cert_dcv_info_requests_correct_url(self, httpx_mock: HTTPXMock):
        fixture = load_fixture("dcv_params.json")
        httpx_mock.add_response(json=fixture)

        with patch("gandi_cli.commands.certificate._get_client") as mock_client:
            mock_client.return_value = GandiClient(token="test-token")
            result = runner.invoke(app, ["cert", "dcv-info", "cert-001"])

        assert result.exit_code == 0
        request = httpx_mock.get_request()
        assert request.method == "POST"
        assert "/certificate/issued-certs/cert-001/dcv_params" in str(request.url)

    def test_cert_dcv_info_with_csr(self, httpx_mock: HTTPXMock, tmp_path):
        fixture = load_fixture("dcv_params.json")
        httpx_mock.add_response(json=fixture)
        csr_file = tmp_path / "test.csr"
        csr_file.write_text("-----BEGIN CERTIFICATE REQUEST-----\ntest\n-----END CERTIFICATE REQUEST-----\n")

        with patch("gandi_cli.commands.certificate._get_client") as mock_client:
            mock_client.return_value = GandiClient(token="test-token")
            result = runner.invoke(app, ["cert", "dcv-info", "cert-001", "--csr", str(csr_file)])

        assert result.exit_code == 0
        request = httpx_mock.get_request()
        body = json.loads(request.content)
        assert "csr" in body

    def test_cert_dcv_info_with_dcv_method(self, httpx_mock: HTTPXMock):
        fixture = load_fixture("dcv_params.json")
        httpx_mock.add_response(json=fixture)

        with patch("gandi_cli.commands.certificate._get_client") as mock_client:
            mock_client.return_value = GandiClient(token="test-token")
            result = runner.invoke(app, ["cert", "dcv-info", "cert-001", "--dcv-method", "dns"])

        assert result.exit_code == 0
        request = httpx_mock.get_request()
        body = json.loads(request.content)
        assert body["dcv_method"] == "dns"

    def test_cert_dcv_info_with_package(self, httpx_mock: HTTPXMock):
        fixture = load_fixture("dcv_params.json")
        httpx_mock.add_response(json=fixture)

        with patch("gandi_cli.commands.certificate._get_client") as mock_client:
            mock_client.return_value = GandiClient(token="test-token")
            result = runner.invoke(app, ["cert", "dcv-info", "cert-001", "--package", "cert_std_1_10_0_digicert"])

        assert result.exit_code == 0
        request = httpx_mock.get_request()
        body = json.loads(request.content)
        assert body["package"] == "cert_std_1_10_0_digicert"


class TestCertDownload:
    """Tests for the certificate download command."""

    def test_cert_download_to_stdout(self, httpx_mock: HTTPXMock):
        pem_text = "-----BEGIN CERTIFICATE-----\nMIItest\n-----END CERTIFICATE-----\n"
        httpx_mock.add_response(text=pem_text, headers={"content-type": "text/plain"})

        with patch("gandi_cli.commands.certificate._get_client") as mock_client:
            mock_client.return_value = GandiClient(token="test-token")
            result = runner.invoke(app, ["cert", "download", "cert-001"])

        assert result.exit_code == 0
        assert "BEGIN CERTIFICATE" in result.stdout
        assert "MIItest" in result.stdout

    def test_cert_download_requests_correct_url(self, httpx_mock: HTTPXMock):
        httpx_mock.add_response(text="pem-data", headers={"content-type": "text/plain"})

        with patch("gandi_cli.commands.certificate._get_client") as mock_client:
            mock_client.return_value = GandiClient(token="test-token")
            result = runner.invoke(app, ["cert", "download", "cert-001"])

        assert result.exit_code == 0
        request = httpx_mock.get_request()
        assert "/certificate/issued-certs/cert-001/crt" in str(request.url)

    def test_cert_download_to_file(self, httpx_mock: HTTPXMock, tmp_path):
        pem_text = "-----BEGIN CERTIFICATE-----\nMIItest\n-----END CERTIFICATE-----\n"
        httpx_mock.add_response(text=pem_text, headers={"content-type": "text/plain"})
        out_file = tmp_path / "cert.pem"

        with patch("gandi_cli.commands.certificate._get_client") as mock_client:
            mock_client.return_value = GandiClient(token="test-token")
            result = runner.invoke(app, ["cert", "download", "cert-001", "--output", str(out_file)])

        assert result.exit_code == 0
        assert "written to" in result.stdout.lower()
        assert out_file.exists()
        content = out_file.read_text()
        assert "BEGIN CERTIFICATE" in content

    def test_cert_download_sends_accept_header(self, httpx_mock: HTTPXMock):
        httpx_mock.add_response(text="pem-data", headers={"content-type": "text/plain"})

        with patch("gandi_cli.commands.certificate._get_client") as mock_client:
            mock_client.return_value = GandiClient(token="test-token")
            result = runner.invoke(app, ["cert", "download", "cert-001"])

        assert result.exit_code == 0
        request = httpx_mock.get_request()
        assert request.headers.get("accept") == "text/plain"
