"""Pytest fixtures for configuration, HTTP client, and API endpoints."""

import pytest
import json
from core.http_client import HttpClient
from endpoints.login import LoginEndpoint

@pytest.fixture(scope="session")
def config():
    """Loads config.json with base_url and other settings."""
    with open("config/config.json") as f:
        return json.load(f)

@pytest.fixture(scope="session")
def http_client(config):
    """Provides shared HTTP client with base_url from config."""
    return HttpClient(config["base_url"])

@pytest.fixture()
def login_endpoint(http_client):
    """Returns LoginEndpoint instance ready to send requests."""
    return LoginEndpoint(http_client)
