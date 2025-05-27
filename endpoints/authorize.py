from requests import Response

from endpoints.base_endpoint import BaseEndpoint


class Authorize(BaseEndpoint):
    def get_token(self, name: str) -> Response:
        response = self._post("/authorize", json={"name": name})
        return response

    def get_token_status(self):
        return self._get(f"/authorize/{self.token}")
