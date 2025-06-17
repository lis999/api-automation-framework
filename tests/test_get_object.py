import allure

from endpoints.object_get import ObjectGet
from utils.assert_helpers import assert_status_code, assert_object_matches_payload


@allure.title("Test getting an object by ID returns correct data")
def test_get_object_by_id(token, created_object_with_cleanup):
    object_id, payload = created_object_with_cleanup
    obj_get = ObjectGet()
    obj_get.set_token(token)

    with allure.step("Get object by ID"):
        response = obj_get.get_object_by_id(object_id)
        assert_status_code(response, 200)
        data = response.json()

    with allure.step("Verify retrieved object fields match original payload"):
        assert data["id"] == object_id
        assert_object_matches_payload(data, payload)
