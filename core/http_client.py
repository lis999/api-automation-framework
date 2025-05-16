import requests

"""HttpClient module provides a wrapper around the 'requests' library 
to standardize and simplify HTTP operations across the framework.

Features:
- Accepts a base_url for consistent endpoint access
- Supports GET, POST, PUT, and DELETE methods
- Automatically builds full request URLs
- Designed for reuse across all API endpoint classes

Usage:
    client = HttpClient("https://api.example.com")
    response = client.post("/login", payload={"user": "name", "pass": "123"})
"""

class HttpClient:
    def __init__(self, base_url):
        self.base_url = base_url.rstrip("/")

    def get(self, path, headers=None):
        return requests.get(f"{self.base_url}{path}", headers=headers)

    def post(self, path, payload=None, headers=None):
        return requests.post(f"{self.base_url}{path}", json=payload, headers=headers)

    def put(self, path, payload=None, headers=None):
        return requests.put(f"{self.base_url}{path}", json=payload, headers=headers)

    def delete(self, path, headers=None):
        return requests.delete(f"{self.base_url}{path}", headers=headers)
    