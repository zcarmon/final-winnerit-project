from api_requests.request_generator import RequestGenerator
from tests.api import CONSTS


class UsersRequestGenerator(RequestGenerator):
    def __init__(self):
        super().__init__(CONSTS.BASE_URL)
        #just for debug purpose
        print("Header = '" + super().get_headers)

    def get_user(self, user_id: int):
        return self.get(f'{CONSTS.USERS_URL}{user_id}')

    def greate_user(self, data: dict):
        return self.post(CONSTS.USERS_URL, data)
