import pytest
import allure
from faker import Faker
from utils.api_client import APIClient

fake = Faker()

@allure.suite("Авторизация пользователя")
class TestLoginUser:

    def setup_method(self):
        self.client = APIClient()
        # создаём тестового пользователя
        self.user = {
            "email": fake.email(),
            "password": "123456",
            "name": fake.first_name()
        }
        response = self.client.create_user(self.user)
        assert response.status_code == 200
        self.token = response.json()["accessToken"].split()[-1]

    def teardown_method(self):
        self.client.delete_user(self.token)

    @allure.title("Успешная авторизация с верными данными")
    def test_login_successfully(self):
        with allure.step("Отправка запроса на логин"):
            response = self.client.login_user({
                "email": self.user["email"],
                "password": self.user["password"]
            })
        assert response.status_code == 200
        assert response.json().get("accessToken") is not None

    @allure.title("Неуспешная авторизация с неверными данными")
    def test_login_with_wrong_credentials(self):
        with allure.step("Отправка запроса на логин с неверным паролем"):
            response = self.client.login_user({
                "email": "wrong@example.com",
                "password": "wrongpass"
            })
        assert response.status_code == 401
