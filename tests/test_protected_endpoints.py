import allure

from endpoints.base_endpoint import BaseEndpoint


@allure.title("GET /meme without token should return 401")
def test_get_all_without_token():
    base = BaseEndpoint()
    response = base._get("/meme")
    assert response.status_code == 401


@allure.title("GET /meme/<id> without token should return 401")
def test_get_by_id_without_token():
    base = BaseEndpoint()
    response = base._get("/meme/1")
    assert response.status_code == 401


@allure.title("POST /meme without token should return 401")
def test_post_without_token():
    base = BaseEndpoint()
    payload = {
        "text": "No auth",
        "url": "https://example.com/unauthorized.jpg",
        "tags": ["unauth"],
        "info": {"author": "none", "type": "image"}
    }
    response = base._post("/meme", json=payload)
    assert response.status_code == 401


@allure.title("PUT /meme/<id> without token should return 401")
def test_put_without_token():
    base = BaseEndpoint()
    payload = {
        "id": 1,
        "text": "Updated",
        "url": "https://example.com/updated.jpg",
        "tags": ["updated"],
        "info": {"author": "none", "type": "image"}
    }
    response = base._put("/meme/1", json=payload)
    assert response.status_code == 401


@allure.title("DELETE /meme/<id> without token should return 401")
def test_delete_without_token():
    base = BaseEndpoint()
    response = base._delete("/meme/1")
    assert response.status_code == 401
