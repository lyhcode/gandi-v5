import httpx
import typer


class GandiAPIError(Exception):
    """Gandi API error with structured error info."""

    def __init__(
        self,
        status_code: int,
        cause: str = "",
        message: str = "",
        object: str = "",
    ):
        self.status_code = status_code
        self.cause = cause
        self.message = message
        self.object = object
        super().__init__(
            f"[{status_code}] {message}" + (f" ({cause})" if cause else "")
        )


class GandiClient:
    BASE_URL = "https://api.gandi.net/v5"
    SANDBOX_URL = "https://api.sandbox.gandi.net/v5"

    def __init__(
        self,
        token: str,
        sharing_id: str | None = None,
        timeout: float = 30.0,
        sandbox: bool = False,
    ):
        self.token = token
        self.sharing_id = sharing_id
        self.sandbox = sandbox
        base_url = self.SANDBOX_URL if sandbox else self.BASE_URL
        self._client = httpx.Client(
            base_url=base_url,
            headers={
                "Authorization": f"Bearer {token}",
                "Content-Type": "application/json",
            },
            timeout=timeout,
        )

    def _inject_sharing_id(self, params: dict | None) -> dict:
        params = params or {}
        if self.sharing_id and "sharing_id" not in params:
            params["sharing_id"] = self.sharing_id
        return params

    def _handle_response(self, response: httpx.Response) -> dict | list | str:
        if response.status_code == 204:
            return {}
        if response.status_code >= 400:
            try:
                data = response.json()
                raise GandiAPIError(
                    status_code=response.status_code,
                    cause=data.get("cause", ""),
                    message=data.get("message", response.text),
                    object=data.get("object", ""),
                )
            except (ValueError, KeyError):
                raise GandiAPIError(
                    status_code=response.status_code,
                    message=response.text,
                )
        content_type = response.headers.get("content-type", "")
        if "application/json" in content_type:
            return response.json()
        return response.text

    def get(
        self,
        path: str,
        params: dict | None = None,
        headers: dict | None = None,
    ) -> dict | list | str:
        params = self._inject_sharing_id(params)
        extra_headers = headers or {}
        response = self._client.get(path, params=params, headers=extra_headers)
        return self._handle_response(response)

    def post(
        self,
        path: str,
        json: dict | None = None,
        params: dict | None = None,
    ) -> dict | list | str:
        params = self._inject_sharing_id(params)
        response = self._client.post(path, json=json, params=params)
        return self._handle_response(response)

    def put(
        self,
        path: str,
        json: dict | None = None,
        params: dict | None = None,
    ) -> dict | list | str:
        response = self._client.put(path, json=json, params=params)
        return self._handle_response(response)

    def patch(
        self,
        path: str,
        json: dict | None = None,
        params: dict | None = None,
    ) -> dict | list | str:
        response = self._client.patch(path, json=json, params=params)
        return self._handle_response(response)

    def delete(
        self,
        path: str,
        params: dict | None = None,
    ) -> dict | list | str:
        response = self._client.delete(path, params=params)
        return self._handle_response(response)

    def close(self):
        self._client.close()

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()
