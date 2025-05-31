# Valid payloads for smoke/happy path testing
valid_payloads = [
    {
        "text": "Valid test",
        "url": "https://example.com/image.jpg",
        "tags": ["test"],
        "info": {"author": "Sergo", "type": "image"}
    },
    {
        "text": "Another valid test",
        "url": "https://example.com/another.jpg",
        "tags": ["test2"],
        "info": {"author": "QA", "type": "image"}
    }
]

# Invalid payloads for negative/regression testing
invalid_payloads = [
    {},  # completely empty
    {"url": "https://example.com/only-url.jpg"},  # missing text, tags, info
    {"text": "Missing info", "url": "https://example.com", "tags": ["tag"]},  # no info
    {"text": "Tags not list", "url": "https://example.com", "tags": "notalist", "info": {"author": "S", "type": "i"}},
    {"text": "Info is string", "url": "https://example.com", "tags": ["t"], "info": "notadict"}
]

# Invalid payloads for PATCH
invalid_patch_payloads = [
    {},  # empty payload
    {"tags": "notalist"},  # wrong type
    {"info": "notadict"},
    {"id": 123456789},  # only ID, no updatable fields
    {"text": None},  # text can't be None
    {"url": 123},  # url should be a string
]

# Invalid payloads for PUT /meme/<id>
invalid_update_payloads = [
    {},  # empty
    {"id": 123},  # missing required fields
    {"id": 123, "text": "bad", "url": "url", "tags": "notalist", "info": {"author": "a", "type": "t"}},  # tags not list
    {"id": 123, "text": "bad", "url": "url", "tags": ["tag"], "info": "notanobject"},  # info not dict
    {"id": 999999, "text": "updated", "url": "https://url", "tags": [], "info": {}}  # unlikely existing ID
]
