def test_login_successfully():
    user = {
        "email": fake.email(),
        "password": "123456",
        "name": fake.first_name()
    }
    reg_response = client.create_user(user)
    login_payload = {"email": user["email"], "password": user["password"]}
    login_response = client.login_user(login_payload)

    assert login_response.status_code == 200
    assert login_response.json().get("accessToken") is not None

    token = reg_response.json()["accessToken"].split()[-1]
    client.delete_user(token)

def test_login_with_wrong_credentials():
    response = client.login_user({
        "email": "wrong@example.com",
        "password": "wrongpass"
    })
    assert response.status_code == 401
