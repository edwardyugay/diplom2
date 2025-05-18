import requests

BASE_URL = "https://stellarburgers.nomoreparties.site/api"

class APIClient:
    def __init__(self):
        self.session = requests.Session()

    def create_user(self, user_data):
        return self.session.post(f"{BASE_URL}/auth/register", json=user_data)

    def login_user(self, credentials):
        return self.session.post(f"{BASE_URL}/auth/login", json=credentials)

    def change_user(self, headers, data):
        return self.session.patch(f"{BASE_URL}/auth/user", headers=headers, json=data)

    def create_order(self, headers, data):
        return self.session.post(f"{BASE_URL}/orders", headers=headers, json=data)

    def get_orders(self, headers=None):
        return self.session.get(f"{BASE_URL}/orders", headers=headers)

    def delete_user(self, token):
        headers = {"Authorization": f"Bearer {token}"}
        return self.session.delete(f"{BASE_URL}/auth/user", headers=headers)
