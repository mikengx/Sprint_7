import allure
import requests
from urls import Urls
from helpers import generate_data_to_register_new_courier_without_login
from helpers import generate_data_to_register_new_courier_without_password
from data import CREATE_COURIER_SUCCESS_RESPONSE


@allure.feature('Создание курьера')
class TestCreateCourier:

    @allure.title('Создание нового курьера')
    def test_create_courier(self, data_for_courier_creation, courier_cleanup):
        with allure.step('Отправляем POST запрос на создание курьера'):
            response = requests.post(f'{Urls.COURIER_CREATE}', json=data_for_courier_creation)
        assert response.status_code == 201 \
            and response.text == CREATE_COURIER_SUCCESS_RESPONSE
        courier_cleanup()

    @allure.title('Создание двух одинаковых курьеров с одинаковыми логинами возвращает ошибку')
    def test_create_courier_existing(self, create_courier_and_cleanup, courier_cleanup):
        with allure.step('Отправляем POST запрос на создание курьера'):
            response = requests.post(f'{Urls.COURIER_CREATE}', json=create_courier_and_cleanup)
        assert response.status_code == 409 \
            and 'Этот логин уже используется' in response.text
        courier_cleanup()

    @allure.title('Создание курьера без логина возвращает ошибку')
    def test_create_courier_without_login(self):
        with allure.step('Отправляем POST запрос на создание курьера'):
            response = requests.post(
                f'{Urls.COURIER_CREATE}',
                generate_data_to_register_new_courier_without_login())
        assert response.status_code == 400 and 'Недостаточно данных для создания учетной записи' in response.text

    @allure.title('Создание курьера без пароля возвращает ошибку')
    def test_create_courier_without_password(self):
        with allure.step('Отправляем POST запрос на создание курьера'):
            response = requests.post(
                f'{Urls.COURIER_CREATE}',
                generate_data_to_register_new_courier_without_password())
        assert response.status_code == 400 and 'Недостаточно данных для создания учетной записи' in response.text
