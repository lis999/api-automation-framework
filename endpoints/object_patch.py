from typing import Dict

from requests import Response

from endpoints.base_endpoint import BaseEndpoint


class ObjectPatch(BaseEndpoint):
    def patch_object(self, object_id: int, partial_payload: Dict) -> Response:
        return self._patch(f"/meme/{object_id}", json=partial_payload)
