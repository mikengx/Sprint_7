import allure
import requests
import pytest
from urls import Urls
from data import Users


@allure.feature('Авторизация курьера')
class TestLoginCourier:

    @allure.title('Авторизация под курьером выдает id')
    def test_courier_log_in(self):
        with allure.step('Отправляем POST запрос на залогинивание курьера'):
            response = requests.post(
                f'{Urls.COURIER_LOGIN}',
                data=Users.data_current)
        assert response.status_code == 200 and 'id' in response.text

    @allure.title('Авторизация курьера с неверным логином/паролем возвращает ошибку')
    def test_courier_log_negative(self):
        with allure.step('Отправляем POST запрос на залогинивание курьера'):
            response = requests.post(
                f'{Urls.COURIER_LOGIN}',
                data=Users.data_negative)
        assert response.status_code == 404 and 'Учетная запись не найдена' in response.text

    @pytest.mark.parametrize('data_without_login_or_password', [Users.data_without_login, Users.data_without_password])
    @allure.title('Авторизация с пустыми логином/паролем возвращает ошибку')
    def test_courier_log_not_all_data(self, data_without_login_or_password):
        with allure.step('Отправляем POST запрос на залогинивание курьера'):
            response = requests.post(
                f'{Urls.COURIER_LOGIN}',
                data=data_without_login_or_password)
        assert response.status_code == 400 and 'Недостаточно данных для входа' in response.text
