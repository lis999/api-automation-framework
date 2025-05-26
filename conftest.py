import pytest

from endpoints.authorize import Authorize


@pytest.fixture(scope="session")
def token():
    auth = Authorize()
    name = "Sergo"

    response = auth.get_token(name)
    assert response.status_code == 200, "Authorization failed"
    token = response.json().get("token")
    assert token, "No token in response"

    auth.set_token(token)
    check_response = auth.is_token_valid()
    assert check_response.status_code == 200, "Token is invalid right after creation"

    return token
