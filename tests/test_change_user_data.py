from utils.api_client import APIClient
from faker import Faker

fake = Faker()

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

    def test_change_user_data_with_auth(self):
        updated = {"name": "UpdatedName"}
        response = self.client.update_user(self.token, updated)
        assert response.status_code == 200
        assert response.json()["user"]["name"] == "UpdatedName"

    def test_change_user_data_without_auth(self):
        updated = {"name": "Hacker"}
        response = self.client.update_user(None, updated)
        assert response.status_code == 401
