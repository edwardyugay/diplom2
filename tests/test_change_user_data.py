import allure
from utils.api_client import APIClient
from data.test_data import generate_user

@allure.suite("Изменение данных пользователя")
class TestChangeUserData:

    def setup_method(self):
        self.client = APIClient()
        self.user = generate_user()
        with allure.step("Создание пользователя через API"):
            response = self.client.create_user(self.user)
        self.token = response.json()["accessToken"].split()[-1]
        self.headers = {"Authorization": f"Bearer {self.token}"}

    def teardown_method(self):
        with allure.step("Удаление пользователя через API"):
            self.client.delete_user(self.token)

    @allure.title("Изменение имени пользователя с авторизацией")
    def test_change_user_data_with_auth(self):
        updated = {"name": "UpdatedName"}
        with allure.step("Отправка запроса на изменение данных"):
            response = self.client.update_user(self.token, updated)
        assert response.status_code == 200
        assert response.json()["user"]["name"] == "UpdatedName"

    @allure.title("Попытка изменения данных без авторизации")
    def test_change_user_data_without_auth(self):
        updated = {"name": "Hacker"}
        with allure.step("Отправка запроса без токена"):
            response = self.client.update_user(None, updated)
        assert response.status_code == 401
