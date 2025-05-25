import allure
import requests


class BaseEndpoint:
    base_url = "https://167.172.172.115:52355"
    token = None
    headers = {}

    def set_token(self, token: str):
        self.token = token
        self.headers = {"Authorization": self.token}

    def _get(self, path, **kwargs):
        url = f"{self.base_url}{path}"
        return requests.get(url, headers=self.headers, **kwargs)

    def _post(self, path, json=None, **kwargs):
        url = f"{self.base_url}{path}"
        return requests.post(url, json=json, headers=self.headers, **kwargs)

    def _put(self, path, json=None, **kwargs):
        url = f"{self.base_url}{path}"
        return requests.put(url, json=json, headers=self.headers, **kwargs)

    def _delete(self, path, **kwargs):
        url = f"{self.base_url}{path}"
        return requests.delete(url, headers=self.headers, **kwargs)

    @allure.step("Check response status code is {expected}")
    def check_status_code(self, response, expected):
        assert response.status_code == expected, f"Expected {expected}, got {response.status_code}"
