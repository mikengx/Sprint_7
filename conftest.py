import pytest
import requests
from urls import Urls
from helpers import generate_data_to_register_new_courier
import allure


@pytest.fixture
def data_for_courier_creation():
    courier_data = generate_data_to_register_new_courier()

    yield courier_data


@pytest.fixture
def create_courier_and_cleanup(data_for_courier_creation):
    with allure.step('Отправляем POST запрос на создание курьера'):
        requests.post(f'{Urls.COURIER_CREATE}', json=data_for_courier_creation)
    
    yield data_for_courier_creation


@pytest.fixture(autouse=True)
def courier_cleanup(request, data_for_courier_creation):
    # Очистка после теста
    created_couriers = []

    def add_courier_for_cleanup():
        # Нужно залогиниться, чтобы получить id для удаления
        courier_data = data_for_courier_creation
        with allure.step('Отправляем POST запрос на залогинивание курьера'):
            courier_login_response = requests.post(f'{Urls.COURIER_LOGIN}', json=courier_data)
        courier_id = courier_login_response.json()["id"]
        created_couriers.append(courier_id)

    def finalizer():
        for courier_id in created_couriers:
            with allure.step('Отправляем DELETE запрос на удаление курьера (cleanup in teardown phase)'):
                requests.delete(f'{Urls.COURIER_DELETE}/{courier_id}')

    request.addfinalizer(finalizer)
    yield add_courier_for_cleanup
