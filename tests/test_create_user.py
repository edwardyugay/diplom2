import pytest
from faker import Faker
from utils.api_client import APIClient

fake = Faker()

def test_create_unique_user():
    client = APIClient()
    user = {
        "email": fake.email(),
        "password": "123456",
        "name": fake.first_name()
    }
    response = client.create_user(user)
    assert response.status_code == 200
    assert response.json().get("success") is True

    # Удаление пользователя после теста
    token = response.json()["accessToken"].split()[-1]
    client.delete_user(token)

@pytest.mark.parametrize("missing_field", ["email", "password", "name"])
def test_create_user_missing_field(missing_field):
    client = APIClient()
    user = {
        "email": fake.email(),
        "password": "123456",
        "name": fake.first_name()
    }
    user.pop(missing_field)
    response = client.create_user(user)
    assert response.status_code == 403
