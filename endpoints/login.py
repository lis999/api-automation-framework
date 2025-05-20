"""LoginEndpoint represents the /login API and provides login-specific actions."""

from core.base_endpoint import BaseEndpoint

class LoginEndpoint(BaseEndpoint):
    def __init__(self, client):
        super().__init__(client, "/login")
