import requests

class HttpClient:
    def __init__(self, base_url):
        self.base_url = base_url.rstrip("/")  # убираем / на конце, если есть

    def get(self, path, headers=None):
        return requests.get(f"{self.base_url}{path}", headers=headers)

    def post(self, path, payload=None, headers=None):
        return requests.post(f"{self.base_url}{path}", json=payload, headers=headers)

    def put(self, path, payload=None, headers=None):
        return requests.put(f"{self.base_url}{path}", json=payload, headers=headers)

    def delete(self, path, headers=None):
        return requests.delete(f"{self.base_url}{path}", headers=headers)
