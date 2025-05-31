import allure

from endpoints.object_get import ObjectGet


@allure.title("Test getting an object by ID returns correct data")
def test_get_object_by_id(token, created_object_with_cleanup):
    object_id = created_object_with_cleanup
    obj_get = ObjectGet()
    obj_get.set_token(token)

    with allure.step("Get object by ID"):
        response = obj_get.get_object_by_id(object_id)
        assert response.status_code == 200
        data = response.json()

    with allure.step("Verify retrieved object fields"):
        assert data["id"] == object_id
        assert data["text"] == "Temp for test"
        assert data["url"] == "https://example.com/temp.jpg"
        assert data["tags"] == ["temp"]
        assert data["info"] == {"author": "Test", "type": "image"}
