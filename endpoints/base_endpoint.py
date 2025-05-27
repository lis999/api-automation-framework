import requests


class BaseEndpoint:
    base_url = "http://167.172.172.115:52355"
    token = None
    headers = {}

    def set_token(self, token: str):
        self.token = token
        self.headers = {"Authorization": token}

    def _get(self, path, headers=None, **kwargs):
        headers = headers or self.headers
        url = f"{self.base_url}{path}"
        return requests.get(url, headers=headers, **kwargs)

    def _post(self, path, json=None, headers=None, **kwargs):
        headers = headers or self.headers
        url = f"{self.base_url}{path}"
        return requests.post(url, json=json, headers=headers, **kwargs)

    def _put(self, path, json=None, headers=None, **kwargs):
        headers = headers or self.headers
        url = f"{self.base_url}{path}"
        return requests.put(url, json=json, headers=headers, **kwargs)

    def _delete(self, path, headers=None, **kwargs):
        headers = headers or self.headers
        url = f"{self.base_url}{path}"
        return requests.delete(url, headers=headers, **kwargs)
