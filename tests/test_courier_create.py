import allure
import requests
from urls import Urls
from helpers import generate_data_to_register_new_courier
from helpers import generate_data_to_register_new_courier_without_login
from helpers import generate_data_to_register_new_courier_without_password
from data import CREATE_COURIER_SUCCESS_RESPONSE


@allure.title('Создание курьера')
class TestCreateCourier:

    @allure.step('Создание нового курьера')
    def test_create_courier(self, create_courier_and_cleanup):
        assert create_courier_and_cleanup.status_code == 201 \
            and create_courier_and_cleanup.text == CREATE_COURIER_SUCCESS_RESPONSE

    @allure.step('Создание двух одинаковых курьеров с одинаковыми логинами возвращает ошибку')
    def test_create_courier_existing(self, create_courier_twice_and_cleanup):
        create_courier_data = generate_data_to_register_new_courier()
        assert create_courier_twice_and_cleanup.status_code == 409 \
            and 'Этот логин уже используется' in create_courier_twice_and_cleanup.text

    @allure.step('Создание курьера без логина возвращает ошибку')
    def test_create_courier_without_login(self):
        response = requests.post(
            f'{Urls.COURIER_CREATE}',
            generate_data_to_register_new_courier_without_login())
        assert response.status_code == 400 and 'Недостаточно данных для создания учетной записи' in response.text

    @allure.step('Создание курьера без пароля возвращает ошибку')
    def test_create_courier_without_password(self):
        response = requests.post(
            f'{Urls.COURIER_CREATE}',
            generate_data_to_register_new_courier_without_password())
        assert response.status_code == 400 and 'Недостаточно данных для создания учетной записи' in response.text
