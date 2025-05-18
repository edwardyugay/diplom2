def test_get_orders_authorized():
    user = {
        "email": fake.email(),
        "password": "123456",
        "name": fake.first_name()
    }
    reg = client.create_user(user)
    token = reg.json()["accessToken"].split()[-1]
    headers = {"Authorization": f"Bearer {token}"}

    response = client.get_orders(headers)
    assert response.status_code == 200
    client.delete_user(token)

def test_get_orders_unauthorized():
    response = client.get_orders()
    assert response.status_code == 401
