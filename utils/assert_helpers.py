def assert_status_code(response, expected_code):
    actual_code = response.status_code
    assert actual_code == expected_code, (
        f"Expected status code {expected_code}, but got {actual_code}. "
        f"Response body: {response.text}"
    )


def assert_token_in_response(response):
    data = response.json()
    assert "token" in data, f"'token' not found in response: {data}"

    token = data["token"]
    assert isinstance(token, str), f"Expected token to be a string, but got {type(token)}"
    assert token.strip(), "Token is empty"


def assert_object_matches_payload(obj: dict, payload: dict):
    for key in ["text", "url", "tags", "info"]:
        assert key in obj, f"Missing key '{key}' in object: {obj}"
        assert key in payload, f"Missing key '{key}' in payload: {payload}"
        assert obj[key] == payload[key], (
            f"Mismatch in field '{key}': expected '{payload[key]}', got '{obj[key]}'"
        )
