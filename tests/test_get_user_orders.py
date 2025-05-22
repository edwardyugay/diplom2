import allure
from faker import Faker
from utils.api_client import APIClient

fake = Faker()

@allure.suite("Получение заказов пользователя")
class TestGetUserOrders:

    def setup_method(self):
        self.client = APIClient()
        self.user = {
            "email": fake.email(),
            "password": "123456",
            "name": fake.first_name()
        }
        response = self.client.create_user(self.user)
        self.token = response.json()["accessToken"].split()[-1]
        self.headers = {"Authorization": f"Bearer {self.token}"}

    def teardown_method(self):
        self.client.delete_user(self.token)

    @allure.title("Получение заказов авторизованного пользователя")
    def test_get_orders_authorized(self):
        with allure.step("Отправка запроса на получение заказов с токеном"):
            response = self.client.get_orders(self.headers)
        assert response.status_code == 200

    @allure.title("Получение заказов без авторизации")
    def test_get_orders_unauthorized(self):
        with allure.step("Отправка запроса без токена"):
            response = self.client.get_orders()
        assert response.status_code == 401
