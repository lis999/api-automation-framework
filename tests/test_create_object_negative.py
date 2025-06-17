import allure
import pytest

from data.create_object_negative_data import invalid_payloads
from endpoints.object_create import ObjectCreate
from utils.assert_helpers import assert_status_code


@allure.title("Test creating object with invalid payload returns 400")
@pytest.mark.parametrize("payload", invalid_payloads)
def test_create_object_invalid_payload(token, payload):
    obj = ObjectCreate()
    obj.set_token(token)

    response = obj.create_object(payload)
    assert_status_code(response, 400)
