import allure

from endpoints.authorize import Authorize
from utils.assert_helpers import assert_status_code


@allure.title("Test successful token generation with valid name")
def test_authorize_success():
    auth = Authorize()
    response = auth.get_token("Sergo")
    assert_status_code(response, 200)
    data = response.json()
    assert "token" in data
    assert isinstance(data["token"], str)
    assert len(data["token"]) > 0


@allure.title("Test authorization with empty name should fail (currently returns 200)")
def test_authorize_empty_name():
    auth = Authorize()
    response = auth.get_token("")
    # Expected: 422
    assert_status_code(response, 422)


@allure.title("Test valid token is accepted by /authorize/<token>")
def test_token_is_valid():
    auth = Authorize()
    response = auth.get_token("Sergo")
    token = response.json().get("token")
    auth.set_token(token)

    check = auth.get_token_status()
    assert_status_code(check, 200)


@allure.title("Test invalid token returns 404 on /authorize/<token>")
def test_invalid_token_status():
    auth = Authorize()
    auth.set_token("this-token-does-not-exist")
    response = auth.get_token_status()
    assert_status_code(response, 404)
