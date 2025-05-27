from requests import Response

from endpoints.base_endpoint import BaseEndpoint


class ObjectGet(BaseEndpoint):
    def get_object_by_id(self, object_id: int) -> Response:
        return self._get(f"/meme/{object_id}")
