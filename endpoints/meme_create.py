import allure

from endpoints.base_endpoint import BaseEndpoint


class MemeCreate(BaseEndpoint):
    @allure.step("Create a new meme")
    def create_meme(self, payload):
        return self._post("/meme", json=payload)
