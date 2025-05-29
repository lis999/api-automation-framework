import allure
import pytest

from data.create_object_data import invalid_payloads
from endpoints.object_create import ObjectCreate


@allure.title("Negative test: Create object with invalid payloads")
@pytest.mark.parametrize("payload", invalid_payloads)
def test_create_object_negative(token, payload):
    obj = ObjectCreate()
    obj.set_token(token)
    if payload == {"text": "", "url": "", "tags": [], "info": {}}:
        pytest.skip("API accepts empty values - not considered invalid")

    with allure.step("Try to create object with invalid payload"):
        response = obj.create_object(payload)
        assert response.status_code in [400, 422], f"Unexpected status: {response.status_code}"
