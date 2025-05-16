"""
BaseEndpoint provides common logic for all API endpoint classes.
It handles sending requests via the shared HttpClient and stores response data.
"""

from core.http_client import HttpClient

class BaseEndpoint:
    def __init__(self, client: HttpClient, endpoint_path: str):
        self.client = client
        self.endpoint_path = endpoint_path
        self.response = None
        self.json = None

    def post(self, payload=None, headers=None):
        self.response = self.client.post(self.endpoint_path, payload, headers)
        self._parse_response()
        return self.response

    def get(self, headers=None):
        self.response = self.client.get(self.endpoint_path, headers)
        self._parse_response()
        return self.response

    def _parse_response(self):
        try:
            self.json = self.response.json()
        except Exception:
            self.json = None
