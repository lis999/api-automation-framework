import allure

from endpoints.object_create import ObjectCreate
from endpoints.object_get import ObjectGet
from endpoints.object_update import ObjectUpdate


@allure.title("Update an object and verify that changes are applied")
def test_update_object(token):
    # Step 1: We create an object
    obj_create = ObjectCreate()
    obj_create.set_token(token)

    payload = {
        "text": "Original object",
        "url": "https://example.com/original.jpg",
        "tags": ["original"],
        "info": {"author": "Sergo", "type": "image"}
    }

    with allure.step("Create an object"):
        response = obj_create.create_object(payload)
        assert response.status_code == 200
        object_id = response.json()["id"]

    # Step 2: We update the created object
    obj_update = ObjectUpdate()
    obj_update.set_token(token)

    updated_payload = {
        "id": object_id,
        "text": "Updated object",
        "url": "https://example.com/updated.jpg",
        "tags": ["updated"],
        "info": {"author": "Sergey", "type": "updated_image"}
    }

    with allure.step("Update the object"):
        update_response = obj_update.update_object(object_id, updated_payload)
        assert update_response.status_code == 200

    # Step 3: We get the updated object
    obj_get = ObjectGet()
    obj_get.set_token(token)

    with allure.step("Get the updated object"):
        get_response = obj_get.get_object_by_id(object_id)
        assert get_response.status_code == 200
        data = get_response.json()

    # Step 4: We compare the updated object fields with the data we used
    with allure.step("Verify the object fields match updated payload"):
        assert str(data["id"]) == str(updated_payload["id"])
        assert data["text"] == updated_payload["text"]
        assert data["url"] == updated_payload["url"]
        assert data["tags"] == updated_payload["tags"]
        assert data["info"] == updated_payload["info"]
