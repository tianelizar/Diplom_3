import string
import random

# генерация данных для создания пользователя
def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

def generate_user_data():
    payload = {
        "email": f'{generate_random_string(10)}@test.com',
        "password": generate_random_string(10),
        "name": generate_random_string(10)
    }
    return payload