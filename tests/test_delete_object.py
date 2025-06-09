import allure

from endpoints.object_delete import ObjectDelete
from endpoints.object_get import ObjectGet
from utils.assert_helpers import assert_status_code


@allure.title("Test deleting an object and verifying it's gone")
def test_delete_object(token, created_object_id):
    obj_delete = ObjectDelete()
    obj_delete.set_token(token)

    with allure.step("Delete the object"):
        delete_response = obj_delete.delete_object(created_object_id)
        assert_status_code(delete_response, 200)

    obj_get = ObjectGet()
    obj_get.set_token(token)

    with allure.step("Verify object is not accessible after deletion"):
        get_response = obj_get.get_object_by_id(created_object_id)
        assert_status_code(get_response, 404)
