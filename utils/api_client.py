import requests
from utils.urls import BASE_URL

class APIClient:
    def create_user(self, data):
        return requests.post(f"{BASE_URL}/auth/register", json=data)

    def delete_user(self, token):
        headers = {"Authorization": f"Bearer {token}"}
        return requests.delete(f"{BASE_URL}/auth/user", headers=headers)

    def update_user(self, token, new_data):
        headers = {"Authorization": f"Bearer {token}"} if token else {}
        return requests.patch(f"{BASE_URL}/auth/user", headers=headers, json=new_data)
