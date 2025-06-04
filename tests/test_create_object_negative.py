import allure
import pytest

from endpoints.object_create import ObjectCreate

invalid_payloads = [
    {},  # completely empty payload
    {"text": "Missing URL"},  # missing required fields
    {
        "text": 123,
        "url": 456,
        "tags": "not a list",
        "info": "not an object"
    },  # invalid field types
]


@pytest.mark.parametrize("payload", invalid_payloads)
@allure.title("Test creating object with invalid payload returns 400 or 422")
def test_create_object_invalid_payload(token, payload):
    obj = ObjectCreate()
    obj.set_token(token)

    response = obj.create_object(payload)
    assert response.status_code == 400, f"Unexpected status: {response.status_code}"
