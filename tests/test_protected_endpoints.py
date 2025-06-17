import allure

from data.create_object_data import single_valid_payload  # пусть будет валидный пэйлоад
from endpoints.base_endpoint import BaseEndpoint
from endpoints.object_create import ObjectCreate
from endpoints.object_delete import ObjectDelete
from utils.assert_helpers import assert_status_code


@allure.title("GET /meme without token should return 401")
def test_get_all_without_token():
    base = BaseEndpoint()
    response = base._get("/meme")
    assert_status_code(response, 401)


@allure.title("GET /meme/<id> without token should return 401")
def test_get_by_id_without_token(token):
    # create object
    obj_create = ObjectCreate()
    obj_create.set_token(token)
    response = obj_create.create_object(single_valid_payload)
    assert_status_code(response, 200)
    object_id = response.json()["id"]

    # check unauthorized access
    base = BaseEndpoint()
    response = base._get(f"/meme/{object_id}")
    assert_status_code(response, 401)

    # cleanup
    obj_delete = ObjectDelete()
    obj_delete.set_token(token)
    obj_delete.delete_object(object_id)


@allure.title("POST /meme without token should return 401")
def test_post_without_token():
    base = BaseEndpoint()
    response = base._post("/meme", json=single_valid_payload)
    assert_status_code(response, 401)


@allure.title("PUT /meme/<id> without token should return 401")
def test_put_without_token(token):
    # create object
    obj_create = ObjectCreate()
    obj_create.set_token(token)
    response = obj_create.create_object(single_valid_payload)
    assert_status_code(response, 200)
    object_id = response.json()["id"]

    # modify payload with same id
    payload = single_valid_payload.copy()
    payload["id"] = object_id
    payload["text"] = "Updated text"

    # check unauthorized PUT
    base = BaseEndpoint()
    response = base._put(f"/meme/{object_id}", json=payload)
    assert_status_code(response, 401)

    # cleanup
    obj_delete = ObjectDelete()
    obj_delete.set_token(token)
    obj_delete.delete_object(object_id)


@allure.title("DELETE /meme/<id> without token should return 401")
def test_delete_without_token(token):
    # create object
    obj_create = ObjectCreate()
    obj_create.set_token(token)
    response = obj_create.create_object(single_valid_payload)
    assert_status_code(response, 200)
    object_id = response.json()["id"]

    # check unauthorized DELETE
    base = BaseEndpoint()
    response = base._delete(f"/meme/{object_id}")
    assert_status_code(response, 401)

    # cleanup
    obj_delete = ObjectDelete()
    obj_delete.set_token(token)
    obj_delete.delete_object(object_id)
