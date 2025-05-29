import allure
import pytest

from endpoints.object_create import ObjectCreate
from endpoints.object_get import ObjectGet
from endpoints.object_patch import ObjectPatch


@pytest.mark.skip(reason="API does not support PATCH method (405)")
@allure.title("Patch an object and verify that changes are applied")
def test_patch_object(token):
    # Step 1: Create a full object
    obj_create = ObjectCreate()
    obj_create.set_token(token)

    payload = {
        "text": "Patch me",
        "url": "https://example.com/patch.jpg",
        "tags": ["original"],
        "info": {"author": "Sergo", "type": "image"}
    }

    with allure.step("Create an object"):
        response = obj_create.create_object(payload)
        assert response.status_code == 200
        object_id = response.json()["id"]

    # Step 2: Patch the object (only change 'text')
    obj_patch = ObjectPatch()
    obj_patch.set_token(token)

    patch_data = {
        "text": "I was patched!"
    }

    with allure.step("Send PATCH request with partial data"):
        patch_response = obj_patch.patch_object(object_id, patch_data)
        assert patch_response.status_code == 200

    # Step 3: Get the object and verify the patch
    obj_get = ObjectGet()
    obj_get.set_token(token)

    with allure.step("Get the patched object"):
        get_response = obj_get.get_object_by_id(object_id)
        assert get_response.status_code == 200
        data = get_response.json()

    with allure.step("Verify patched fields and unchanged fields"):
        assert data["text"] == patch_data["text"]
        assert data["url"] == payload["url"]
        assert data["tags"] == payload["tags"]
        assert data["info"] == payload["info"]
