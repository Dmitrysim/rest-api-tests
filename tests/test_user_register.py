import allure
from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.requests_lib import RequestsLib


@allure.epic("User register cases")
class TestUserRegister(BaseCase):

    @allure.description("Create user successfully")
    def test_create_user_successfully(self):
        data = self.prepare_registration_data()

        response = RequestsLib.post("/user", data=data)

        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, "id")

    @allure.description("Create user with existing email")
    def test_create_user_with_existing_email(self):
        email='vinkotov@example.com'
        data = self.prepare_registration_data(email)

        response = RequestsLib.post("/user", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"Users with email '{email}' already exists"
