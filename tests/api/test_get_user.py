import pytest
import requests
from pytest_check import check
from api_requests.users_request_generator import UsersRequestGenerator
from tests.api import CONSTS
from tests.api.CONSTS import *

#Without parameters
@pytest.mark.api
def test_get_user():
    response = requests.get("https://reqres.in/api/users/2",
                            headers = {CONSTS.X_API_KEY_FIELD: CONSTS.X_API_KEY_VALUE})

    # Soft validation
    #Use this for specific issue cause in case of failure
    #it should indicate rolling failures שגיאה מתגלגלת :-)
    check.equal(response.status_code, STATUS_CODE_OK)
    check.equal(response.json()["data"]["id"] , 2)
    check.equal(response.json()["data"]["email"] , "janet.weaver@reqres.in")

    #Hard validation
    assert response.status_code == STATUS_CODE_OK
    assert response.json()["data"]["id"] == 2
    assert response.json()["data"]["email"] == "janet.weaver@reqres.in"
    pass

#With parameters
@pytest.mark.api
def test_get_user_with_generator():
    response = UsersRequestGenerator().get_user(2)
    UsersRequestGenerator.validate_status_code(response)
    UsersRequestGenerator.validate_data(response,["data","id"], 2)
    UsersRequestGenerator.validate_data(response,["data","email"], "janet.weaver@reqres.in")

    generator = UsersRequestGenerator()
    print(generator.get_headers)