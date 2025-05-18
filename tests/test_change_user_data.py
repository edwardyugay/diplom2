def test_change_user_data_with_auth():
    user = {
        "email": fake.email(),
        "password": "123456",
        "name": fake.first_name()
    }
    reg = client.create_user(user)
    token = reg.json()["accessToken"].split()[-1]
    headers = {"Authorization": f"Bearer {token}"}
    response = client.change_user(headers, {"name": "UpdatedName"})
    assert response.status_code == 200
    assert response.json()["user"]["name"] == "UpdatedName"
    client.delete_user(token)

def test_change_user_data_without_auth():
    response = client.change_user({}, {"name": "Hacker"})
    assert response.status_code == 401
