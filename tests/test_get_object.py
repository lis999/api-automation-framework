import allure

from endpoints.object_create import ObjectCreate
from endpoints.object_get import ObjectGet


@allure.title("Get object by ID and verify returned data")
def test_get_object_by_id(token):
    obj_create = ObjectCreate()
    obj_create.set_token(token)

    payload = {
        "text": "Get this meme",
        "url": "https://example.com/get.jpg",
        "tags": ["check", "get"],
        "info": {"author": "Sergey", "type": "image"}
    }

    with allure.step("Create a new object"):
        create_response = obj_create.create_object(payload)
        assert create_response.status_code == 200, f"Create failed: {create_response.status_code}"
        created = create_response.json()
        object_id = created["id"]

    object_get = ObjectGet()
    object_get.set_token(token)

    with allure.step("Get object by ID"):
        get_response = object_get.get_object_by_id(object_id)
        assert get_response.status_code == 200, f"Get failed: {get_response.status_code}"
        received = get_response.json()

    with allure.step("Compare response data with original payload"):
        assert received["id"] == object_id
        assert received["text"] == payload["text"]
        assert received["url"] == payload["url"]
        assert received["tags"] == payload["tags"]
        assert received["info"] == payload["info"]
