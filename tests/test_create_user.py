import pytest
import allure
from faker import Faker
from utils.api_client import APIClient

fake = Faker()

@allure.suite("Регистрация пользователя")
class TestCreateUser:

    def setup_method(self):
        self.client = APIClient()

    @allure.title("Уникальный пользователь: позитивный сценарий")
    def test_create_unique_user(self):
        user = {
            "email": fake.email(),
            "password": "123456",
            "name": fake.first_name()
        }
        with allure.step("Отправка запроса на регистрацию нового пользователя"):
            response = self.client.create_user(user)
        assert response.status_code == 200
        assert response.json().get("success") is True

        token = response.json()["accessToken"].split()[-1]
        with allure.step("Удаление тестового пользователя через API"):
            self.client.delete_user(token)

    @pytest.mark.parametrize("missing_field", ["email", "password", "name"])
    @allure.title("Регистрация без обязательного поля: негативный сценарий")
    def test_create_user_missing_field(self, missing_field):
        user = {
            "email": fake.email(),
            "password": "123456",
            "name": fake.first_name()
        }
        user.pop(missing_field)
        with allure.step(f"Отправка запроса без поля '{missing_field}'"):
            response = self.client.create_user(user)
        assert response.status_code == 403
