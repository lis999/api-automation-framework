from requests import Response

from endpoints.base_endpoint import BaseEndpoint


class ObjectDelete(BaseEndpoint):
    def delete_object(self, object_id: int) -> Response:
        return self._delete(f"/meme/{object_id}")
