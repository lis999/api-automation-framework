import allure

from endpoints.authorize import Authorize


@allure.title("Test successful token generation with valid name")
def test_authorize_success():
    auth = Authorize()
    response = auth.get_token("Sergo")
    assert response.status_code == 200
    data = response.json()
    assert "token" in data
    assert isinstance(data["token"], str)
    assert len(data["token"]) > 0


@allure.title("Test authorization with empty name should fail (currently returns 200)")
def test_authorize_empty_name():
    auth = Authorize()
    response = auth.get_token("")
    # Expected: 400 or 422
    assert response.status_code in [400, 422], f"Expected failure, got {response.status_code}"


@allure.title("Test valid token is accepted by /authorize/<token>")
def test_token_is_valid():
    auth = Authorize()
    response = auth.get_token("Sergo")
    token = response.json().get("token")
    auth.set_token(token)

    check = auth.get_token_status()
    assert check.status_code == 200


@allure.title("Test invalid token returns 404 on /authorize/<token>")
def test_invalid_token_status():
    auth = Authorize()
    auth.set_token("this-token-does-not-exist")
    response = auth.get_token_status()
    assert response.status_code == 404
