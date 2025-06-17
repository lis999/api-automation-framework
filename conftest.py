import pytest

from endpoints.authorize import Authorize
from endpoints.object_create import ObjectCreate
from endpoints.object_delete import ObjectDelete


@pytest.fixture(scope="session")
def token():
    auth = Authorize()
    name = "Sergo"

    response = auth.get_token(name)
    assert response.status_code == 200, "Authorization failed"
    token = response.json().get("token")
    assert token, "No token in response"

    auth.set_token(token)
    check_response = auth.get_token_status()
    assert check_response.status_code == 200, "Token is invalid right after creation"

    return token


@pytest.fixture
def created_object_id(token):
    obj = ObjectCreate()
    obj.set_token(token)

    payload = {
        "text": "To be deleted",
        "url": "https://example.com/delete.jpg",
        "tags": ["delete"],
        "info": {"author": "Sergo", "type": "image"}
    }

    response = obj.create_object(payload)
    assert response.status_code == 200
    return response.json()["id"]


@pytest.fixture
def created_object_with_cleanup(token):
    obj_create = ObjectCreate()
    obj_create.set_token(token)

    payload = {
        "text": "Temp for test",
        "url": "https://example.com/temp.jpg",
        "tags": ["temp"],
        "info": {"author": "Test", "type": "image"}
    }

    response = obj_create.create_object(payload)
    assert response.status_code == 200
    object_id = response.json()["id"]

    yield object_id, payload  # return ID and payload

    # cleanup after test
    obj_delete = ObjectDelete()
    obj_delete.set_token(token)
    obj_delete.delete_object(object_id)
