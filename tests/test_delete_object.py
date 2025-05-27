import allure

from endpoints.object_create import ObjectCreate
from endpoints.object_delete import ObjectDelete
from endpoints.object_get import ObjectGet


@allure.title("Delete an object and verify it returns 404 when fetched")
def test_delete_object(token):
    # Step 1: create an object
    obj_create = ObjectCreate()
    obj_create.set_token(token)

    payload = {
        "text": "To be deleted",
        "url": "https://example.com/delete.jpg",
        "tags": ["delete"],
        "info": {"author": "Sergo", "type": "image"}
    }

    with allure.step("Create an object"):
        response = obj_create.create_object(payload)
        assert response.status_code == 200
        object_id = response.json()["id"]

    # Step 2: delete the object
    obj_delete = ObjectDelete()
    obj_delete.set_token(token)

    with allure.step("Delete the object"):
        delete_response = obj_delete.delete_object(object_id)
        assert delete_response.status_code == 200

    # Step 3: try to get the deleted object
    obj_get = ObjectGet()
    obj_get.set_token(token)

    with allure.step("Try to get the deleted object"):
        get_response = obj_get.get_object_by_id(object_id)
        assert get_response.status_code == 404
