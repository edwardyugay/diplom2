import allure
from faker import Faker
from utils.api_client import APIClient
from data.test_data import TEST_INGREDIENT

fake = Faker()

@allure.suite("Создание заказа")
class TestCreateOrder:

    def setup_method(self):
        self.client = APIClient()
        self.user = {
            "email": fake.email(),
            "password": "123456",
            "name": fake.first_name()
        }
        with allure.step("Создание пользователя через API"):
            response = self.client.create_user(self.user)
        self.token = response.json()["accessToken"].split()[-1]
        self.headers = {"Authorization": f"Bearer {self.token}"}

    def teardown_method(self):
        with allure.step("Удаление пользователя через API"):
            self.client.delete_user(self.token)

    @allure.title("Создание заказа с авторизацией и ингредиентами")
    def test_create_order_with_auth_and_ingredients(self):
        with allure.step("Отправка запроса на создание заказа"):
            response = self.client.create_order(self.headers, {"ingredients": [TEST_INGREDIENT]})
        assert response.status_code == 200
        assert response.json().get("success") is True

    @allure.title("Создание заказа без авторизации")
    def test_create_order_without_auth(self):
        with allure.step("Отправка запроса без токена"):
            response = self.client.create_order(None, {"ingredients": [TEST_INGREDIENT]})
        assert response.status_code == 401

    @allure.title("Создание заказа без ингредиентов")
    def test_create_order_without_ingredients(self):
        with allure.step("Отправка запроса с пустым списком ингредиентов"):
            response = self.client.create_order(self.headers, {"ingredients": []})
        assert response.status_code == 400

    @allure.title("Создание заказа с неверным hash ингредиентов")
    def test_create_order_with_invalid_ingredients(self):
        with allure.step("Отправка запроса с невалидным идентификатором ингредиента"):
            response = self.client.create_order(self.headers, {"ingredients": ["invalid_hash"]})
        assert response.status_code == 500
