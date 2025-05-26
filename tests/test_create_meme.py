import pytest

from endpoints.meme_create import MemeCreate


@pytest.mark.smoke
def test_create_meme_success(token):
    meme = MemeCreate()
    meme.set_token(token)

    payload = {
        "text": "My first meme",
        "url": "https://example.com/meme.jpg",
        "tags": ["funny", "test"],
        "info": {"author": "Sergey", "type": "image"}
    }

    response = meme.create_meme(payload)
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"

    data = response.json()
    assert "id" in data, "Response JSON has no 'id'"
    assert data["text"] == payload["text"], "Text mismatch"
    assert data["url"] == payload["url"], "URL mismatch"
    assert data["tags"] == payload["tags"], "Tags mismatch"
    assert data["info"] == payload["info"], "Info mismatch"
