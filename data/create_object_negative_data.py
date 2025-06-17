invalid_payloads = [
    {},  # completely empty payload
    {"text": "Missing URL"},  # missing required fields
    {
        "text": 123,
        "url": 456,
        "tags": "not a list",
        "info": "not an object"
    },  # invalid field types
]
