import allure
import requests
from urls import Urls
from helpers import register_new_courier
from helpers import register_new_courier_without_login
from helpers import register_new_courier_without_password


class TestCreateCourier:
    create_courier_data = register_new_courier()

    @allure.title('Создание курьера')
    def test_create_courier(self):
        response_body = '{"ok":true}'
        response = requests.post(
            f'{Urls.COURIER_CREATE}',
            TestCreateCourier.create_courier_data)
        assert response.status_code == 201 and response.text == response_body

    @allure.title('Нельзя создать двух одинаковых курьеров с одинаковыми логинами')
    def test_create_courier_existing(self):
        response = requests.post(
            f'{Urls.COURIER_CREATE}',
            TestCreateCourier.create_courier_data)
        assert response.status_code == 409 and 'Этот логин уже используется' in response.text

    @allure.title('Нельзя создать курьера без логина')
    def test_create_courier_without_login(self):
        response = requests.post(
            f'{Urls.COURIER_CREATE}',
            register_new_courier_without_login())
        assert response.status_code == 400 and 'Недостаточно данных для создания учетной записи' in response.text

    @allure.title('Нельзя создать курьера без пароля')
    def test_create_courier_without_password(self):
        response = requests.post(
            f'{Urls.COURIER_CREATE}',
            register_new_courier_without_password())
        assert response.status_code == 400 and 'Недостаточно данных для создания учетной записи' in response.text
