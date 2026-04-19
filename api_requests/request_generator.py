import operator
from functools import reduce
import requests
from pytest_check import check
from requests import Response
from tests.api import CONSTS


class RequestGenerator:
    def __init__(self, base_url: str, headers: dict = CONSTS.HEADER):
        self.__base_url = base_url
        self.__headers = headers

    @property
    def get_headers(self) -> str:
        return str(self.__headers)

    def get(self, end_point: str) :
        return requests.get(f"{self.__base_url}{end_point}", headers=self.__headers)

    def post(self, end_point: str, data: dict):
        return requests.get(f"{self.__base_url}{end_point}", json=data, headers=self.__headers)


    def validate_status_code(response: Response, expected_response_code : int = CONSTS.STATUS_CODE_OK):
        """
        Validates the supplied status code. By default validates {CONSTS.STATUS_CODE_OK}
        """
        #soft validation
        # Use this for specific issue cause in case of failure
        # it should indicate rolling failures שגיאה מתגלגלת :-)
        check.equal(response.status_code, expected_response_code)

        # hard validation
        assert (response.status_code, expected_response_code)
        pass

    def validate_data(response: Response, the_field : list, the_value):
        # soft validation
        # Use this for specific issue cause in case of failure
        # it should indicate rolling failures שגיאה מתגלגלת :-)
        actual_value = reduce(operator.getitem, the_field, response.json())
        check.equal(actual_value, the_value)

        # hard validation
        assert actual_value == the_value
        pass