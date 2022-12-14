import allure
from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.requests_lib import RequestsLib


@allure.epic("User get cases")
class TestUserGet(BaseCase):

    @allure.description("Get user without auth")
    def test_get_user_details_not_auth(self):
        response = RequestsLib.get("/user/2")

        Assertions.assert_json_has_not_key(response, "username")
        Assertions.assert_json_has_not_key(response, "email")
        Assertions.assert_json_has_not_key(response, "firstName")
        Assertions.assert_json_has_not_key(response, "lastName")

    @allure.description("Get user with auth")
    def test_get_user_details_auth_as_same_user(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }

        response1 = RequestsLib.get("/user/login", data=data)

        auth_sid = self.get_cookie(response1, "auth_sid")
        token = self.get_header(response1, "x-csrf-token")
        user_id_from_auth_method = self.get_json_value(response1, "user_id")

        response2 = RequestsLib.get(
            f"/user/{user_id_from_auth_method}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )

        expected_fiels = ["username", "email", "firstName", "lastName"]

        Assertions.assert_json_has_keys(response2, expected_fiels)
