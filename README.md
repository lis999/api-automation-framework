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

## How to run tests

### Run all functional tests:

pytest -v --alluredir=allure-results

## Generate Allure HTML reort:

allure serve allure-results

## Run Locust UI:

locust -f performance/locustfile.py --host=http://167.172.172.115:52355
