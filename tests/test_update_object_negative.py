import allure
import pytest

from data.create_object_data import invalid_update_payloads
from endpoints.object_update import ObjectUpdate


@allure.title("Negative test: Update object with invalid payloads")
@pytest.mark.parametrize("payload", invalid_update_payloads)
def test_update_object_negative(token, payload):
    obj = ObjectUpdate()
    obj.set_token(token)

    with allure.step("Try to update object with invalid payload"):
        object_id = payload.get("id", 999999)  # default ID for test if not provided
        response = obj.update_object(object_id, payload)
        assert response.status_code in [400, 403, 404, 422], f"Unexpected status: {response.status_code}"
