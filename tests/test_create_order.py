def test_create_order_with_auth_and_ingredients():
    user = {
        "email": fake.email(),
        "password": "123456",
        "name": fake.first_name()
    }
    reg = client.create_user(user)
    token = reg.json()["accessToken"].split()[-1]
    headers = {"Authorization": f"Bearer {token}"}

    # Пример ингредиента (замени на актуальный id)
    ingredients = {"ingredients": ["61c0c5a71d1f82001bdaaa6d"]}
    response = client.create_order(headers, ingredients)
    assert response.status_code == 200
    client.delete_user(token)

def test_create_order_without_ingredients():
    response = client.create_order({}, {"ingredients": []})
    assert response.status_code == 400
