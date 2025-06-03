import allure

from endpoints.object_create import ObjectCreate


@allure.title("Test creating object with completely empty payload returns 400")
def test_create_object_empty_payload(token):
    obj = ObjectCreate()
    obj.set_token(token)

    payload = {}  # no fields

    response = obj.create_object(payload)
    assert response.status_code == 400


@allure.title("Test creating object with invalid field types returns 422")
def test_create_object_invalid_field_types(token):
    obj = ObjectCreate()
    obj.set_token(token)

    payload = {
        "text": 123,  # should be string
        "url": 456,  # should be string
        "tags": "notalist",  # should be list
        "info": "notanobject"  # should be dict
    }

    response = obj.create_object(payload)
    assert response.status_code == 400


@allure.title("Test creating object with missing some required fields returns 400")
def test_create_object_missing_some_fields(token):
    obj = ObjectCreate()
    obj.set_token(token)

    payload = {
        "text": "Missing fields"
        # no url, tags, info
    }

    response = obj.create_object(payload)
    assert response.status_code == 400
