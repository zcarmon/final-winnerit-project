import pytest
import requests
from tests.api.CONSTS import *


@pytest.mark.api
def test_login_user():
    response = requests.get("https://reqres.in/api/login", headers=HEADER)

    assert response.status_code == STATUS_CODE_OK
    assert response.json()["_meta"]["powered_by"] == "ReqRes"
