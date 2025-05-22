from faker import Faker

fake = Faker()

def generate_user():
    return {
        "email": fake.email(),
        "password": "123456",
        "name": fake.first_name()
    }

def generate_user_with_missing_field(field):
    user = generate_user()
    user.pop(field)
    return user
