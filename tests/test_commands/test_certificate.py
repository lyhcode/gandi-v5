"""Tests for certificate commands."""

import json
import subprocess
from pathlib import Path
from unittest.mock import patch, MagicMock

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
        assert "dns" in result.stdout.lower()

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
        # PATCH to set DCV method, then POST to fetch params
        httpx_mock.add_response(json={}, method="PATCH")
        httpx_mock.add_response(json=fixture, method="POST")

        with patch("gandi_cli.commands.certificate._get_client") as mock_client:
            mock_client.return_value = GandiClient(token="test-token")
            result = runner.invoke(app, ["cert", "dcv-info", "cert-001", "--dcv-method", "dns"])

        assert result.exit_code == 0
        requests = httpx_mock.get_requests()
        # First request: PATCH to set DCV method
        assert requests[0].method == "PATCH"
        assert "/certificate/issued-certs/cert-001/dcv" in str(requests[0].url)
        patch_body = json.loads(requests[0].content)
        assert patch_body["dcv_method"] == "dns"
        # Second request: POST to fetch DCV params
        assert requests[1].method == "POST"
        assert "/dcv_params" in str(requests[1].url)

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


class TestCertCsr:
    """Tests for the certificate CSR generation command."""

    def test_cert_csr_generates_files(self, tmp_path):
        def fake_openssl(cmd, **kwargs):
            # Simulate openssl writing the key and CSR files
            for i, arg in enumerate(cmd):
                if arg == "-keyout" and i + 1 < len(cmd):
                    Path(cmd[i + 1]).write_text("-----BEGIN PRIVATE KEY-----\nfake\n-----END PRIVATE KEY-----\n")
                if arg == "-out" and i + 1 < len(cmd):
                    Path(cmd[i + 1]).write_text("-----BEGIN CERTIFICATE REQUEST-----\nfake\n-----END CERTIFICATE REQUEST-----\n")
            return subprocess.CompletedProcess(cmd, 0, stdout="", stderr="")

        with patch("gandi_cli.commands.certificate.subprocess.run", side_effect=fake_openssl):
            result = runner.invoke(app, ["cert", "csr", "example.com", "-d", str(tmp_path)])

        assert result.exit_code == 0
        assert "example.com.key" in result.stdout
        assert "example.com.csr" in result.stdout

    def test_cert_csr_passes_correct_args_to_openssl(self, tmp_path):
        captured_cmd = []

        def fake_openssl(cmd, **kwargs):
            captured_cmd.extend(cmd)
            for i, arg in enumerate(cmd):
                if arg == "-keyout" and i + 1 < len(cmd):
                    Path(cmd[i + 1]).write_text("key")
                if arg == "-out" and i + 1 < len(cmd):
                    Path(cmd[i + 1]).write_text("csr")
            return subprocess.CompletedProcess(cmd, 0, stdout="", stderr="")

        with patch("gandi_cli.commands.certificate.subprocess.run", side_effect=fake_openssl):
            result = runner.invoke(app, ["cert", "csr", "example.com", "-d", str(tmp_path)])

        assert result.exit_code == 0
        assert "openssl" in captured_cmd
        assert "req" in captured_cmd
        assert "-sha256" in captured_cmd
        assert "rsa:2048" in captured_cmd
        assert "-nodes" in captured_cmd
        assert "/CN=example.com" in captured_cmd

    def test_cert_csr_refuses_to_overwrite_key(self, tmp_path):
        key_file = tmp_path / "example.com.key"
        key_file.write_text("existing key")

        with patch("gandi_cli.commands.certificate.subprocess.run") as mock_run:
            result = runner.invoke(app, ["cert", "csr", "example.com", "-d", str(tmp_path)])

        assert result.exit_code == 1
        # openssl should never have been called
        mock_run.assert_not_called()
        # key file should be untouched
        assert key_file.read_text() == "existing key"

    def test_cert_csr_custom_subject(self, tmp_path):
        captured_cmd = []

        def fake_openssl(cmd, **kwargs):
            captured_cmd.extend(cmd)
            for i, arg in enumerate(cmd):
                if arg == "-keyout" and i + 1 < len(cmd):
                    Path(cmd[i + 1]).write_text("key")
                if arg == "-out" and i + 1 < len(cmd):
                    Path(cmd[i + 1]).write_text("csr")
            return subprocess.CompletedProcess(cmd, 0, stdout="", stderr="")

        with patch("gandi_cli.commands.certificate.subprocess.run", side_effect=fake_openssl):
            result = runner.invoke(app, [
                "cert", "csr", "example.com", "-d", str(tmp_path),
                "--subject", "/C=FR/O=Example/CN=example.com",
            ])

        assert result.exit_code == 0
        assert "/C=FR/O=Example/CN=example.com" in captured_cmd

    def test_cert_csr_openssl_not_found(self, tmp_path):
        with patch("gandi_cli.commands.certificate.subprocess.run", side_effect=FileNotFoundError):
            result = runner.invoke(app, ["cert", "csr", "example.com", "-d", str(tmp_path)])

        assert result.exit_code == 1

    def test_cert_csr_openssl_failure(self, tmp_path):
        failed = subprocess.CompletedProcess(["openssl"], 1, stdout="", stderr="some error")
        with patch("gandi_cli.commands.certificate.subprocess.run", return_value=failed):
            result = runner.invoke(app, ["cert", "csr", "example.com", "-d", str(tmp_path)])

        assert result.exit_code == 1

    def test_cert_csr_creates_output_dir(self, tmp_path):
        out_dir = tmp_path / "subdir" / "nested"

        def fake_openssl(cmd, **kwargs):
            for i, arg in enumerate(cmd):
                if arg == "-keyout" and i + 1 < len(cmd):
                    Path(cmd[i + 1]).write_text("key")
                if arg == "-out" and i + 1 < len(cmd):
                    Path(cmd[i + 1]).write_text("csr")
            return subprocess.CompletedProcess(cmd, 0, stdout="", stderr="")

        with patch("gandi_cli.commands.certificate.subprocess.run", side_effect=fake_openssl):
            result = runner.invoke(app, ["cert", "csr", "example.com", "-d", str(out_dir)])

        assert result.exit_code == 0
        assert out_dir.exists()


class TestCertIssue:
    """Tests for the certificate issue command."""

    def test_cert_issue(self, httpx_mock: HTTPXMock, tmp_path):
        fixture = load_fixture("issue_response.json")
        httpx_mock.add_response(json=fixture)
        csr_file = tmp_path / "test.csr"
        csr_file.write_text("-----BEGIN CERTIFICATE REQUEST-----\ntest\n-----END CERTIFICATE REQUEST-----\n")

        with patch("gandi_cli.commands.certificate._get_client") as mock_client:
            mock_client.return_value = GandiClient(token="test-token")
            result = runner.invoke(app, [
                "cert", "issue",
                "--csr", str(csr_file),
                "--package", "cert_std_1_10_0_digicert",
            ])

        assert result.exit_code == 0
        assert "order submitted" in result.stdout.lower()

    def test_cert_issue_sends_correct_url(self, httpx_mock: HTTPXMock, tmp_path):
        fixture = load_fixture("issue_response.json")
        httpx_mock.add_response(json=fixture)
        csr_file = tmp_path / "test.csr"
        csr_file.write_text("-----BEGIN CERTIFICATE REQUEST-----\ntest\n-----END CERTIFICATE REQUEST-----\n")

        with patch("gandi_cli.commands.certificate._get_client") as mock_client:
            mock_client.return_value = GandiClient(token="test-token")
            result = runner.invoke(app, [
                "cert", "issue",
                "--csr", str(csr_file),
                "--package", "cert_std_1_10_0_digicert",
            ])

        assert result.exit_code == 0
        request = httpx_mock.get_request()
        assert request.method == "POST"
        url = str(request.url)
        assert url.endswith("/certificate/issued-certs") or "/certificate/issued-certs?" in url

    def test_cert_issue_sends_csr_and_package_in_body(self, httpx_mock: HTTPXMock, tmp_path):
        fixture = load_fixture("issue_response.json")
        httpx_mock.add_response(json=fixture)
        csr_file = tmp_path / "test.csr"
        csr_file.write_text("-----BEGIN CERTIFICATE REQUEST-----\ntest\n-----END CERTIFICATE REQUEST-----\n")

        with patch("gandi_cli.commands.certificate._get_client") as mock_client:
            mock_client.return_value = GandiClient(token="test-token")
            result = runner.invoke(app, [
                "cert", "issue",
                "--csr", str(csr_file),
                "--package", "cert_std_1_10_0_digicert",
            ])

        assert result.exit_code == 0
        request = httpx_mock.get_request()
        body = json.loads(request.content)
        assert "BEGIN CERTIFICATE REQUEST" in body["csr"]
        assert body["package"] == "cert_std_1_10_0_digicert"

    def test_cert_issue_with_dcv_method(self, httpx_mock: HTTPXMock, tmp_path):
        fixture = load_fixture("issue_response.json")
        httpx_mock.add_response(json=fixture)
        csr_file = tmp_path / "test.csr"
        csr_file.write_text("-----BEGIN CERTIFICATE REQUEST-----\ntest\n-----END CERTIFICATE REQUEST-----\n")

        with patch("gandi_cli.commands.certificate._get_client") as mock_client:
            mock_client.return_value = GandiClient(token="test-token")
            result = runner.invoke(app, [
                "cert", "issue",
                "--csr", str(csr_file),
                "--package", "cert_std_1_10_0_digicert",
                "--dcv-method", "dns",
            ])

        assert result.exit_code == 0
        request = httpx_mock.get_request()
        body = json.loads(request.content)
        assert body["dcv_method"] == "dns"

    def test_cert_issue_with_altnames(self, httpx_mock: HTTPXMock, tmp_path):
        fixture = load_fixture("issue_response.json")
        httpx_mock.add_response(json=fixture)
        csr_file = tmp_path / "test.csr"
        csr_file.write_text("-----BEGIN CERTIFICATE REQUEST-----\ntest\n-----END CERTIFICATE REQUEST-----\n")

        with patch("gandi_cli.commands.certificate._get_client") as mock_client:
            mock_client.return_value = GandiClient(token="test-token")
            result = runner.invoke(app, [
                "cert", "issue",
                "--csr", str(csr_file),
                "--package", "cert_std_3_10_0_digicert",
                "--altnames", "www.example.com, api.example.com",
            ])

        assert result.exit_code == 0
        request = httpx_mock.get_request()
        body = json.loads(request.content)
        assert body["altnames"] == ["www.example.com", "api.example.com"]

    def test_cert_issue_dry_run(self, httpx_mock: HTTPXMock, tmp_path):
        httpx_mock.add_response(json={})
        csr_file = tmp_path / "test.csr"
        csr_file.write_text("-----BEGIN CERTIFICATE REQUEST-----\ntest\n-----END CERTIFICATE REQUEST-----\n")

        with patch("gandi_cli.commands.certificate._get_client") as mock_client:
            mock_client.return_value = GandiClient(token="test-token")
            result = runner.invoke(app, [
                "cert", "issue",
                "--csr", str(csr_file),
                "--package", "cert_std_1_10_0_digicert",
                "--dry-run",
            ])

        assert result.exit_code == 0
        assert "dry run" in result.stdout.lower()
        request = httpx_mock.get_request()
        assert request.headers.get("dry-run") == "1"

    def test_cert_issue_shows_certificate_id(self, httpx_mock: HTTPXMock, tmp_path):
        fixture = load_fixture("issue_response.json")
        httpx_mock.add_response(json=fixture)
        csr_file = tmp_path / "test.csr"
        csr_file.write_text("-----BEGIN CERTIFICATE REQUEST-----\ntest\n-----END CERTIFICATE REQUEST-----\n")

        with patch("gandi_cli.commands.certificate._get_client") as mock_client:
            mock_client.return_value = GandiClient(token="test-token")
            result = runner.invoke(app, [
                "cert", "issue",
                "--csr", str(csr_file),
                "--package", "cert_std_1_10_0_digicert",
            ])

        assert result.exit_code == 0
        assert "cert-003" in result.stdout

    def test_cert_issue_missing_csr_file(self):
        with patch("gandi_cli.commands.certificate._get_client") as mock_client:
            mock_client.return_value = GandiClient(token="test-token")
            result = runner.invoke(app, [
                "cert", "issue",
                "--csr", "/nonexistent/file.csr",
                "--package", "cert_std_1_10_0_digicert",
            ])

        assert result.exit_code == 1


class TestJsonOutput:
    """Tests for JSON output format across all certificate commands."""

    def _patch_json_format(self):
        """Patch state.output_format to 'json'."""
        return patch("gandi_cli.main.state.output_format", "json")

    def test_cert_list_json_returns_raw_api_data(self, httpx_mock: HTTPXMock):
        fixture = load_fixture("certificates.json")
        httpx_mock.add_response(json=fixture)

        with patch("gandi_cli.commands.certificate._get_client") as mock_client, \
             self._patch_json_format():
            mock_client.return_value = GandiClient(token="test-token")
            result = runner.invoke(app, ["cert", "list"])

        assert result.exit_code == 0
        parsed = json.loads(result.stdout)
        assert isinstance(parsed, list)
        assert len(parsed) == 2
        # Raw data should preserve nested structure
        assert isinstance(parsed[0]["dates"], dict)
        assert isinstance(parsed[0]["package"], dict)
        assert "starts_at" in parsed[0]["dates"]

    def test_cert_info_json_returns_raw_api_data(self, httpx_mock: HTTPXMock):
        fixture = load_fixture("certificate_detail.json")
        httpx_mock.add_response(json=fixture)

        with patch("gandi_cli.commands.certificate._get_client") as mock_client, \
             self._patch_json_format():
            mock_client.return_value = GandiClient(token="test-token")
            result = runner.invoke(app, ["cert", "info", "cert-001"])

        assert result.exit_code == 0
        parsed = json.loads(result.stdout)
        assert parsed["id"] == "cert-001"
        # Raw data should preserve nested structure
        assert isinstance(parsed["dates"], dict)
        assert isinstance(parsed["altnames"], list)

    def test_cert_issue_json(self, httpx_mock: HTTPXMock, tmp_path):
        fixture = load_fixture("issue_response.json")
        httpx_mock.add_response(json=fixture)
        csr_file = tmp_path / "test.csr"
        csr_file.write_text("-----BEGIN CERTIFICATE REQUEST-----\ntest\n-----END CERTIFICATE REQUEST-----\n")

        with patch("gandi_cli.commands.certificate._get_client") as mock_client, \
             self._patch_json_format():
            mock_client.return_value = GandiClient(token="test-token")
            result = runner.invoke(app, [
                "cert", "issue",
                "--csr", str(csr_file),
                "--package", "cert_std_1_10_0_digicert",
            ])

        assert result.exit_code == 0
        parsed = json.loads(result.stdout)
        assert parsed["id"] == "cert-003"
        # No human-readable messages mixed in
        assert "order submitted" not in result.stdout.lower()

    def test_cert_reissue_json(self, httpx_mock: HTTPXMock, tmp_path):
        fixture = load_fixture("reissue_response.json")
        httpx_mock.add_response(json=fixture)
        csr_file = tmp_path / "test.csr"
        csr_file.write_text("-----BEGIN CERTIFICATE REQUEST-----\ntest\n-----END CERTIFICATE REQUEST-----\n")

        with patch("gandi_cli.commands.certificate._get_client") as mock_client, \
             self._patch_json_format():
            mock_client.return_value = GandiClient(token="test-token")
            result = runner.invoke(app, ["cert", "reissue", "cert-001", "--csr", str(csr_file)])

        assert result.exit_code == 0
        parsed = json.loads(result.stdout)
        assert parsed["message"] == "Certificate Reissue Submitted"
        assert "reissue submitted" not in result.stdout

    def test_cert_dcv_info_json(self, httpx_mock: HTTPXMock):
        fixture = load_fixture("dcv_params.json")
        # PATCH to set DCV method, then POST to fetch params
        httpx_mock.add_response(json={}, method="PATCH")
        httpx_mock.add_response(json=fixture, method="POST")

        with patch("gandi_cli.commands.certificate._get_client") as mock_client, \
             self._patch_json_format():
            mock_client.return_value = GandiClient(token="test-token")
            result = runner.invoke(app, ["cert", "dcv-info", "cert-001", "--dcv-method", "dns"])

        assert result.exit_code == 0
        parsed = json.loads(result.stdout)
        assert parsed["dcv_method"] == "dns"
        assert isinstance(parsed["fqdns"], list)
        assert parsed["fqdns"][0] == "example.com"
        assert isinstance(parsed["raw_messages"], list)

    def test_cert_download_json(self, httpx_mock: HTTPXMock):
        pem_text = "-----BEGIN CERTIFICATE-----\nMIItest\n-----END CERTIFICATE-----\n"
        httpx_mock.add_response(text=pem_text, headers={"content-type": "text/plain"})

        with patch("gandi_cli.commands.certificate._get_client") as mock_client, \
             self._patch_json_format():
            mock_client.return_value = GandiClient(token="test-token")
            result = runner.invoke(app, ["cert", "download", "cert-001"])

        assert result.exit_code == 0
        parsed = json.loads(result.stdout)
        assert parsed["id"] == "cert-001"
        assert "BEGIN CERTIFICATE" in parsed["certificate"]

    def test_cert_csr_json(self, tmp_path):
        def fake_openssl(cmd, **kwargs):
            for i, arg in enumerate(cmd):
                if arg == "-keyout" and i + 1 < len(cmd):
                    Path(cmd[i + 1]).write_text("key")
                if arg == "-out" and i + 1 < len(cmd):
                    Path(cmd[i + 1]).write_text("csr")
            return subprocess.CompletedProcess(cmd, 0, stdout="", stderr="")

        with patch("gandi_cli.commands.certificate.subprocess.run", side_effect=fake_openssl), \
             self._patch_json_format():
            result = runner.invoke(app, ["cert", "csr", "example.com", "-d", str(tmp_path)])

        assert result.exit_code == 0
        parsed = json.loads(result.stdout)
        assert parsed["key"].endswith("example.com.key")
        assert parsed["csr"].endswith("example.com.csr")
        # No human-readable messages mixed in
        assert "Key:" not in result.stdout


class TestCertDcvInfoExoDns:
    """Tests for --exo-dns flag on dcv-info command."""

    def test_exo_dns_outputs_cname_command(self, httpx_mock: HTTPXMock):
        fixture = load_fixture("dcv_params.json")
        # --exo-dns implies --dcv-method dns → PATCH then POST
        httpx_mock.add_response(json={}, method="PATCH")
        httpx_mock.add_response(json=fixture, method="POST")

        with patch("gandi_cli.commands.certificate._get_client") as mock_client:
            mock_client.return_value = GandiClient(token="test-token")
            result = runner.invoke(app, ["cert", "dcv-info", "cert-001", "--exo-dns"])

        assert result.exit_code == 0
        assert "exo dns add CNAME example.com" in result.stdout
        assert "-n _acme-challenge" in result.stdout
        assert "-a dcv-token-abc123.comodoca.com" in result.stdout

    def test_exo_dns_implies_dcv_method_dns(self, httpx_mock: HTTPXMock):
        """--exo-dns should automatically set --dcv-method dns via PATCH."""
        fixture = load_fixture("dcv_params.json")
        # PATCH to set DCV method dns, then POST to fetch params
        httpx_mock.add_response(json={}, method="PATCH")
        httpx_mock.add_response(json=fixture, method="POST")

        with patch("gandi_cli.commands.certificate._get_client") as mock_client:
            mock_client.return_value = GandiClient(token="test-token")
            result = runner.invoke(app, ["cert", "dcv-info", "cert-001", "--exo-dns"])

        assert result.exit_code == 0
        requests = httpx_mock.get_requests()
        # PATCH sets the DCV method
        assert requests[0].method == "PATCH"
        patch_body = json.loads(requests[0].content)
        assert patch_body["dcv_method"] == "dns"

    def test_exo_dns_respects_explicit_dcv_method(self, httpx_mock: HTTPXMock):
        """Explicit --dcv-method should not be overridden by --exo-dns."""
        fixture = load_fixture("dcv_params.json")
        # PATCH to set DCV method http, then POST to fetch params
        httpx_mock.add_response(json={}, method="PATCH")
        httpx_mock.add_response(json=fixture, method="POST")

        with patch("gandi_cli.commands.certificate._get_client") as mock_client:
            mock_client.return_value = GandiClient(token="test-token")
            result = runner.invoke(app, [
                "cert", "dcv-info", "cert-001",
                "--exo-dns", "--dcv-method", "http",
            ])

        requests = httpx_mock.get_requests()
        # PATCH should use the explicit method
        patch_body = json.loads(requests[0].content)
        assert patch_body["dcv_method"] == "http"

    def test_exo_dns_outputs_multiple_commands(self, httpx_mock: HTTPXMock):
        fixture = load_fixture("dcv_params_multi.json")
        # --exo-dns implies --dcv-method dns → PATCH then POST
        httpx_mock.add_response(json={}, method="PATCH")
        httpx_mock.add_response(json=fixture, method="POST")

        with patch("gandi_cli.commands.certificate._get_client") as mock_client:
            mock_client.return_value = GandiClient(token="test-token")
            result = runner.invoke(app, ["cert", "dcv-info", "cert-001", "--exo-dns"])

        assert result.exit_code == 0
        lines = [l for l in result.stdout.strip().splitlines() if l.startswith("exo")]
        assert len(lines) == 2
        assert "-n _acme-challenge " in lines[0]
        assert "-n _acme-challenge.www " in lines[1]

    def test_exo_dns_json_mode(self, httpx_mock: HTTPXMock):
        fixture = load_fixture("dcv_params_multi.json")
        # --exo-dns implies --dcv-method dns → PATCH then POST
        httpx_mock.add_response(json={}, method="PATCH")
        httpx_mock.add_response(json=fixture, method="POST")

        with patch("gandi_cli.commands.certificate._get_client") as mock_client, \
             patch("gandi_cli.main.state.output_format", "json"):
            mock_client.return_value = GandiClient(token="test-token")
            result = runner.invoke(app, ["cert", "dcv-info", "cert-001", "--exo-dns"])

        assert result.exit_code == 0
        parsed = json.loads(result.stdout)
        assert "commands" in parsed
        assert len(parsed["commands"]) == 2
        assert parsed["commands"][0].startswith("exo dns add")

    def test_exo_dns_with_string_fqdns_and_raw_messages(self, httpx_mock: HTTPXMock):
        """Handle real API shape where fqdns is a list of strings."""
        fixture = load_fixture("dcv_params_strings.json")
        # --exo-dns implies --dcv-method dns → PATCH then POST
        httpx_mock.add_response(json={}, method="PATCH")
        httpx_mock.add_response(json=fixture, method="POST")

        with patch("gandi_cli.commands.certificate._get_client") as mock_client:
            mock_client.return_value = GandiClient(token="test-token")
            result = runner.invoke(app, ["cert", "dcv-info", "cert-001", "--exo-dns"])

        assert result.exit_code == 0
        assert "exo dns add CNAME example.com" in result.stdout
        assert "-n _acme-challenge" in result.stdout
        assert "-a dcv-token-abc123.comodoca.com" in result.stdout

    def test_exo_dns_falls_back_to_dns_records(self, httpx_mock: HTTPXMock):
        """Falls back to parsing dns_records when raw_messages is absent."""
        fixture = {
            "dcv_method": "dns",
            "fqdns": ["example.com"],
            "dns_records": [
                "_dnsauth.example.com. 10800 IN CNAME _token.dcv.digicert.com."
            ],
            "messages": [
                "Please add the following DNS record: _dnsauth.example.com. 10800 IN CNAME _token.dcv.digicert.com."
            ]
        }
        # --exo-dns implies --dcv-method dns → PATCH then POST
        httpx_mock.add_response(json={}, method="PATCH")
        httpx_mock.add_response(json=fixture, method="POST")

        with patch("gandi_cli.commands.certificate._get_client") as mock_client:
            mock_client.return_value = GandiClient(token="test-token")
            result = runner.invoke(app, ["cert", "dcv-info", "cert-001", "--exo-dns"])

        assert result.exit_code == 0
        assert "exo dns add CNAME example.com" in result.stdout
        assert "-n _dnsauth" in result.stdout
        assert "-a _token.dcv.digicert.com" in result.stdout

    def test_exo_dns_no_records_shows_message(self, httpx_mock: HTTPXMock):
        """Shows message when no DNS records can be extracted."""
        fixture = {"dcv_method": "email", "fqdns": ["example.com"]}
        # PATCH to set DCV method email, then POST to fetch params
        httpx_mock.add_response(json={}, method="PATCH")
        httpx_mock.add_response(json=fixture, method="POST")

        with patch("gandi_cli.commands.certificate._get_client") as mock_client:
            mock_client.return_value = GandiClient(token="test-token")
            result = runner.invoke(app, [
                "cert", "dcv-info", "cert-001",
                "--exo-dns", "--dcv-method", "email",
            ])

        assert "No DNS records" in result.output

    def test_exo_dns_without_flag_shows_normal_output(self, httpx_mock: HTTPXMock):
        fixture = load_fixture("dcv_params.json")
        httpx_mock.add_response(json=fixture)

        with patch("gandi_cli.commands.certificate._get_client") as mock_client:
            mock_client.return_value = GandiClient(token="test-token")
            result = runner.invoke(app, ["cert", "dcv-info", "cert-001"])

        assert result.exit_code == 0
        assert "exo dns" not in result.stdout


class TestFqdnToExoArgs:
    """Tests for the _fqdn_to_exo_args helper."""

    def test_simple_subdomain(self):
        from gandi_cli.commands.certificate import _fqdn_to_exo_args
        name, domain = _fqdn_to_exo_args("_acme-challenge.example.com")
        assert name == "_acme-challenge"
        assert domain == "example.com"

    def test_deep_subdomain(self):
        from gandi_cli.commands.certificate import _fqdn_to_exo_args
        name, domain = _fqdn_to_exo_args("_acme-challenge.www.example.com")
        assert name == "_acme-challenge.www"
        assert domain == "example.com"

    def test_bare_domain(self):
        from gandi_cli.commands.certificate import _fqdn_to_exo_args
        name, domain = _fqdn_to_exo_args("example.com")
        assert name == ""
        assert domain == "example.com"

    def test_cctld(self):
        from gandi_cli.commands.certificate import _fqdn_to_exo_args
        name, domain = _fqdn_to_exo_args("_acme-challenge.example.co.uk")
        assert name == "_acme-challenge"
        assert domain == "example.co.uk"

    def test_trailing_dot(self):
        from gandi_cli.commands.certificate import _fqdn_to_exo_args
        name, domain = _fqdn_to_exo_args("_acme-challenge.example.com.")
        assert name == "_acme-challenge"
        assert domain == "example.com"
