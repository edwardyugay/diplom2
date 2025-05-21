import allure
from utils.api_client import APIClient
from faker import Faker

fake = Faker()

@allure.suite("Изменение данных пользователя")
class TestChangeUserData:

    def setup_method(self):
        self.client = APIClient()
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

    @allure.title("Изменение данных пользователя с авторизацией")
    def test_change_user_data_with_auth(self):
        updated = {"name": "UpdatedName"}
        response = self.client.update_user(self.token, updated)
        assert response.status_code == 200
        assert response.json()["user"]["name"] == "UpdatedName"

    @allure.title("Попытка изменить данные без авторизации")
    def test_change_user_data_without_auth_
