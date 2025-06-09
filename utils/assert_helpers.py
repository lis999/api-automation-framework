def assert_object_matches_payload(obj: dict, payload: dict):
    assert obj["text"] == payload["text"], f"Expected text '{payload['text']}', got '{obj['text']}'"
    assert obj["url"] == payload["url"], f"Expected url '{payload['url']}', got '{obj['url']}'"
    assert obj["tags"] == payload["tags"], f"Expected tags {payload['tags']}, got {obj['tags']}"
    assert obj["info"] == payload["info"], f"Expected info {payload['info']}, got {obj['info']}"


def assert_status_code(response, expected_code):
    actual_code = response.status_code
    assert actual_code == expected_code, f"Expected {expected_code}, got {actual_code}"
