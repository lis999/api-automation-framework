import allure
import pytest

from endpoints.object_update import ObjectUpdate
from utils.assert_helpers import assert_status_code


@allure.title("Test updating object with bad request payload returns 400")
@pytest.mark.parametrize("payload", [
    {"tags": "not a list"},
    {"info": "not an object"},
])
def test_update_object_bad_request(token, created_object_with_cleanup, payload):
    object_id = created_object_with_cleanup
    obj = ObjectUpdate()
    obj.set_token(token)
    response = obj.update_object(object_id, {"id": object_id, **payload})
    assert_status_code(response, 400)


@allure.title("Test updating non-existent object returns 404")
def test_update_object_not_found(token):
    obj = ObjectUpdate()
    obj.set_token(token)

    payload = {
        "id": 999999,
        "text": "Trying to update non-existent object",
        "url": "https://example.com/non-existent.jpg",
        "tags": ["fake"],
        "info": {"author": "ghost", "type": "image"}
    }

    response = obj.update_object(payload["id"], payload)
    assert_status_code(response, 404)
