import random
import string


# метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки
def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string

def generate_data_to_register_new_courier():
    login = generate_random_string(10)
    password = generate_random_string(10)
    firstName = generate_random_string(10)
    reg_data = {
        "login": login,
        "password": password,
        "name": firstName
    }
    return reg_data

def generate_data_to_register_new_courier_without_login():
    password = generate_random_string(10)
    firstName = generate_random_string(10)
    reg_data = {
        "password": password,
        "name": firstName
    }
    return reg_data

def generate_data_to_register_new_courier_without_password():
    login = generate_random_string(10)
    firstName = generate_random_string(10)
    reg_data = {
        "login": login,
        "name": firstName
    }
    return reg_data
