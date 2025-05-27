from typing import Dict, Any

from requests import Response

from endpoints.base_endpoint import BaseEndpoint


class ObjectUpdate(BaseEndpoint):
    def update_object(self, object_id: int, payload: Dict[str, Any]) -> Response:
        return self._put(f"/meme/{object_id}", json=payload)
