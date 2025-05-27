import allure
import pytest

from endpoints.object_create import ObjectCreate


@allure.title("Create object and verify response fields")
@pytest.mark.smoke
def test_create_object_success(token):
    obj_new = ObjectCreate()
    obj_new.set_token(token)

    payload = {
        "text": "My first meme",
        "url": "https://example.com/meme.jpg",
        "tags": ["funny", "test"],
        "info": {"author": "Sergey", "type": "image"}
    }

    with allure.step("Send POST request to create object"):
        response = obj_new.create_object(payload)
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"

    with allure.step("Verify response fields match payload"):
        data = response.json()
        assert "id" in data, "Response JSON has no 'id'"
        assert data["text"] == payload["text"], "Text mismatch"
        assert data["url"] == payload["url"], "URL mismatch"
        assert data["tags"] == payload["tags"], "Tags mismatch"
        assert data["info"] == payload["info"], "Info mismatch"
