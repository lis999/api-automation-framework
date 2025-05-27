from typing import Dict

import allure
from requests import Response

from endpoints.base_endpoint import BaseEndpoint


class ObjectCreate(BaseEndpoint):
    @allure.step("Create a new object")
    def create_object(self, payload: Dict) -> Response:
        return self._post("/meme", json=payload)
