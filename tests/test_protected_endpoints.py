import allure
import requests

BASE_URL = "http://167.172.172.115:52355"


@allure.title("GET /meme without token should fail")
def test_get_all_objects_unauthorized():
    response = requests.get(f"{BASE_URL}/meme")
    assert response.status_code in [401, 403]


@allure.title("POST /meme without token should fail")
def test_create_object_unauthorized():
    payload = {
        "text": "Should fail",
        "url": "https://example.com/fail.jpg",
        "tags": ["fail"],
        "info": {"author": "None", "type": "image"}
    }
    response = requests.post(f"{BASE_URL}/meme", json=payload)
    assert response.status_code in [401, 403]


@allure.title("PUT /meme/<id> without token should fail")
def test_update_object_unauthorized():
    payload = {
        "id": 123456,
        "text": "Updated",
        "url": "https://example.com/updated.jpg",
        "tags": ["new"],
        "info": {"author": "None", "type": "image"}
    }
    response = requests.put(f"{BASE_URL}/meme/123456", json=payload)
    assert response.status_code in [401, 403, 404]  # 404 also possible for nonexistent ID


@allure.title("DELETE /meme/<id> without token should fail")
def test_delete_object_unauthorized():
    response = requests.delete(f"{BASE_URL}/meme/123456")
    assert response.status_code in [401, 403, 404]


@allure.title("GET /meme/<id> without token should fail")
def test_get_object_by_id_unauthorized():
    response = requests.get(f"{BASE_URL}/meme/123456")
    assert response.status_code in [401, 403, 404]
