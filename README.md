# api-automation-framework

# API Automation Framework with Locust

This project is a complete API automation framework built with **Python**, **Pytest**, **Allure**, and **Locust**.

It is designed to test the behavior of a simple meme-sharing API, covering both functionality and performance.

---

## Features

- Data-driven positive and negative API testing
- Allure reports with step annotations
- Token-based authentication
- Modular endpoint structure
- Load testing using Locust
- Pre-commit ready and flake8/black compatible

## Project structure

api-automation-framework/
│
├── endpoints/ # Each endpoint in a separate file
│ ├── base_endpoint.py
│ ├── object_create.py
│ ├── object_get.py
│ ├── object_update.py
│ ├── object_delete.py
│ └── object_patch.py (skipped - API unsupported)
│
├── tests/ # Functional API tests
│ ├── test_create_object.py
│ ├── test_create_object_negative.py
│ ├── test_get_object.py
│ ├── test_update_object.py
│ ├── test_update_object_negative.py
│ ├── test_delete_object.py
│ └── test_patch_object.py (skipped)
│
├── data/ # Test payloads
│ └── create_object_data.py
│
├── performance/ # Locust load testing
│ └── locustfile.py
│
├── conftest.py # Shared Pytest fixtures
├── requirements.txt
├── pyproject.toml
└── README.md

## Authorization Endpoint Tests

These tests ensure that `/authorize` endpoint works as expected:

- `POST /authorize` with valid name returns a token
- `POST /authorize` with empty name fails (currently returns 200 — test fails intentionally)
- `GET /authorize/<token>` returns 200 if token is valid
- `GET /authorize/<invalid_token>` returns 404

## Unauthorized Access Tests

These tests verify that all protected endpoints are inaccessible without a token:

- `GET /meme` → should return 401/403
- `POST /meme` → should return 401/403
- `GET /meme/<id>` → should return 401/403/404
- `PUT /meme/<id>` → should return 401/403/404
- `DELETE /meme/<id>` → should return 401/403/404

These tests directly use `requests` to bypass token injection.

## How to run tests

### Run all functional tests:

pytest -v --alluredir=allure-results

## Generate Allure HTML reort:

allure serve allure-results

## Run Locust UI:

locust -f performance/locustfile.py --host=http://167.172.172.115:52355
