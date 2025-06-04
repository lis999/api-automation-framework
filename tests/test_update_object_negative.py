import allure
import pytest

from endpoints.object_update import ObjectUpdate


@allure.title("Test updating object with bad request payload returns 400")
@pytest.mark.parametrize("payload", [
    {"id": 123, "tags": "not a list"},
    {"id": 123, "info": "not an object"},
])
def test_update_object_bad_request(token, payload):
    obj = ObjectUpdate()
    obj.set_token(token)
    response = obj.update_object(payload["id"], payload)
    assert response.status_code == 403


@allure.title("Test updating non-existent object returns 404")
@pytest.mark.parametrize("payload", [
    {"id": 999999, "text": "Trying to update non-existent object"},
])
def test_update_object_not_found(token, payload):
    obj = ObjectUpdate()
    obj.set_token(token)
    response = obj.update_object(payload["id"], payload)
    assert response.status_code == 404
