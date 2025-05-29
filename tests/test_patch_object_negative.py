import allure
import pytest

from data.create_object_data import invalid_patch_payloads
from endpoints.object_patch import ObjectPatch


@pytest.mark.skip(reason="API does not support PATCH method (405)")
@allure.title("Negative test: Patch object with invalid data")
@pytest.mark.parametrize("patch_data", invalid_patch_payloads)
def test_patch_object_negative(token, patch_data):
    obj_patch = ObjectPatch()
    obj_patch.set_token(token)

    object_id = 999999  # use nonexistent ID for safety

    with allure.step("Try to PATCH object with invalid data"):
        response = obj_patch.patch_object(object_id, patch_data)
        assert response.status_code in [400, 404, 422], f"Unexpected status: {response.status_code}"
