from endpoints.base_endpoint import BaseEndpoint


class Authorize(BaseEndpoint):
    def get_token(self, name: str):
        response = self._post("/authorize", json={"name": name})
        return response

    def is_token_valid(self):
        return self._get(f"/authorize/{self.token}")
