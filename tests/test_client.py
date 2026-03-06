import pytest
import httpx
from pytest_httpx import HTTPXMock

from gandi_cli.client import GandiClient, GandiAPIError


BASE_URL = "https://api.gandi.net/v5"


@pytest.fixture
def client():
    c = GandiClient(token="test-api-token")
    yield c
    c.close()


@pytest.fixture
def client_with_sharing_id():
    c = GandiClient(token="test-api-token", sharing_id="org-abc123")
    yield c
    c.close()


class TestAuthHeader:
    def test_auth_header_is_set(self, httpx_mock: HTTPXMock, client: GandiClient):
        httpx_mock.add_response(
            url=f"{BASE_URL}/domain/domains",
            json={"data": "ok"},
        )
        client.get("/domain/domains")

        request = httpx_mock.get_request()
        assert request.headers["authorization"] == "Bearer test-api-token"

    def test_content_type_header_is_set(self, httpx_mock: HTTPXMock, client: GandiClient):
        httpx_mock.add_response(
            url=f"{BASE_URL}/domain/domains",
            json={"data": "ok"},
        )
        client.get("/domain/domains")

        request = httpx_mock.get_request()
        assert request.headers["content-type"] == "application/json"


class TestSharingIdInjection:
    def test_sharing_id_injected_when_set(
        self, httpx_mock: HTTPXMock, client_with_sharing_id: GandiClient
    ):
        httpx_mock.add_response(json={"data": "ok"})
        client_with_sharing_id.get("/domain/domains")

        request = httpx_mock.get_request()
        assert "sharing_id=org-abc123" in str(request.url)

    def test_sharing_id_not_injected_when_not_set(
        self, httpx_mock: HTTPXMock, client: GandiClient
    ):
        httpx_mock.add_response(json={"data": "ok"})
        client.get("/domain/domains")

        request = httpx_mock.get_request()
        assert "sharing_id" not in str(request.url)

    def test_sharing_id_not_overridden_if_already_in_params(
        self, httpx_mock: HTTPXMock, client_with_sharing_id: GandiClient
    ):
        httpx_mock.add_response(json={"data": "ok"})
        client_with_sharing_id.get(
            "/domain/domains", params={"sharing_id": "custom-id"}
        )

        request = httpx_mock.get_request()
        assert "sharing_id=custom-id" in str(request.url)
        assert "sharing_id=org-abc123" not in str(request.url)


class TestSuccessfulJsonResponse:
    def test_get_json_response(self, httpx_mock: HTTPXMock, client: GandiClient):
        expected = [{"fqdn": "example.com"}, {"fqdn": "example.org"}]
        httpx_mock.add_response(json=expected)

        result = client.get("/domain/domains")
        assert result == expected

    def test_post_json_response(self, httpx_mock: HTTPXMock, client: GandiClient):
        expected = {"message": "Domain created"}
        httpx_mock.add_response(json=expected)

        result = client.post("/domain/domains", json={"fqdn": "example.com"})
        assert result == expected


class TestErrorHandling:
    def test_401_raises_gandi_api_error(
        self, httpx_mock: HTTPXMock, client: GandiClient
    ):
        httpx_mock.add_response(
            status_code=401,
            json={
                "cause": "Unauthorized",
                "message": "Invalid API key",
                "object": "HTTPUnauthorized",
            },
        )

        with pytest.raises(GandiAPIError) as exc_info:
            client.get("/domain/domains")

        err = exc_info.value
        assert err.status_code == 401
        assert err.cause == "Unauthorized"
        assert err.message == "Invalid API key"
        assert err.object == "HTTPUnauthorized"
        assert "401" in str(err)
        assert "Invalid API key" in str(err)

    def test_404_raises_gandi_api_error(
        self, httpx_mock: HTTPXMock, client: GandiClient
    ):
        httpx_mock.add_response(
            status_code=404,
            json={
                "cause": "Not Found",
                "message": "The resource could not be found.",
                "object": "HTTPNotFound",
            },
        )

        with pytest.raises(GandiAPIError) as exc_info:
            client.get("/domain/domains/nonexistent.com")

        err = exc_info.value
        assert err.status_code == 404
        assert err.cause == "Not Found"
        assert err.message == "The resource could not be found."


class TestSpecialResponses:
    def test_204_returns_empty_dict(self, httpx_mock: HTTPXMock, client: GandiClient):
        httpx_mock.add_response(status_code=204)

        result = client.delete("/domain/domains/example.com/records/test")
        assert result == {}

    def test_text_plain_response_returns_string(
        self, httpx_mock: HTTPXMock, client: GandiClient
    ):
        httpx_mock.add_response(
            text="@ 300 IN A 192.0.2.1",
            headers={"content-type": "text/plain"},
        )

        result = client.get(
            "/domain/domains/example.com/records",
            headers={"Accept": "text/plain"},
        )
        assert result == "@ 300 IN A 192.0.2.1"
        assert isinstance(result, str)
