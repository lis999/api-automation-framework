import allure
import pytest

from data.update_object_data import updated_payload
from endpoints.object_get import ObjectGet
from endpoints.object_update import ObjectUpdate
from utils.assert_helpers import assert_status_code, assert_object_matches_payload


@allure.title("Positive test: Update object with valid payload")
@pytest.mark.smoke
def test_update_object(token, created_object_with_cleanup):
    object_id, original_payload = created_object_with_cleanup

    obj_update = ObjectUpdate()
    obj_update.set_token(token)

    payload = {
        "id": object_id,
        **updated_payload
    }

    with allure.step("Send PUT request to update object"):
        response = obj_update.update_object(object_id, payload)
        assert_status_code(response, 200)

    obj_get = ObjectGet()
    obj_get.set_token(token)

    with allure.step("Get the updated object"):
        get_response = obj_get.get_object_by_id(object_id)
        assert_status_code(get_response, 200)

    with allure.step("Verify updated object fields match payload"):
        data = get_response.json()
        assert int(data["id"]) == object_id
        assert_object_matches_payload(data, updated_payload)
