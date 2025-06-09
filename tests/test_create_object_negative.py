import allure
import pytest

from endpoints.object_create import ObjectCreate
from utils.assert_helpers import assert_status_code

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
@allure.title("Test creating object with invalid payload returns 400")
def test_create_object_invalid_payload(token, payload):
    obj = ObjectCreate()
    obj.set_token(token)

    response = obj.create_object(payload)
    assert_status_code(response, 400)
