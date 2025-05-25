import allure

from endpoints.base_endpoint import BaseEndpoint


class Authorize(BaseEndpoint):
    @allure.step("Authorize user with name: {name}")
    def get_token(self, name: str):
        response = self._post("/authorize", json={"name": name})
        self.check_status_code(response, 200)
        token = response.json().get("token")
        assert token, "No token received"
        self.set_token(token)
        return token

    @allure.step("Check if token is still valid")
    def is_token_valid(self):
        response = self._get(f"/authorize/{self.token}")
        return response.status_code == 200
