import pytest
import requests
from urls import Urls
from helpers import generate_data_to_register_new_courier


@pytest.fixture
def create_courier_and_cleanup():
    """Фикстура создает курьера и возвращает данные для теста, удаляет после"""
    courier_data = generate_data_to_register_new_courier()
    response = requests.post(f'{Urls.COURIER_CREATE}', json=courier_data)
    
    # Проверяем успешное создание
    assert response.status_code == 201, f"Setup failed - не удалось создать курьера: {response.text}"
        
    yield response
    
    # Очистка после теста
    # Нужно залогиниться, чтобы получить id для удаления
    courier_login_response = requests.post(f'{Urls.COURIER_LOGIN}', json=courier_data)
    assert courier_login_response.status_code == 200, f"Teardown failed - не удалось залогиниться: {courier_login_response.text}"
    courier_login_response_json = courier_login_response.json()
    courier_id = courier_login_response_json["id"]
    courier_delete_response = requests.delete(f'{Urls.COURIER_DELETE}/{courier_id}')
    assert courier_delete_response.status_code == 200, f"Teardown failed - не удалось удалить курьера: {courier_delete_response.text}"


@pytest.fixture
def create_courier_twice_and_cleanup():
    """Фикстура создает курьера дважды и возвращает данные для теста, удаляет после"""
    courier_data = generate_data_to_register_new_courier()
    # create courier for the first time:
    response_initial = requests.post(f'{Urls.COURIER_CREATE}', json=courier_data)
    # Проверяем успешное создание
    assert response_initial.status_code == 201, f"Setup failed - не удалось создать курьера: {response_initial.text}"
    # re-create the same courier:
    response_duplicate = requests.post(f'{Urls.COURIER_CREATE}', json=courier_data)

    yield response_duplicate

    # Очистка после теста
    # Нужно залогиниться, чтобы получить id для удаления
    courier_login_response = requests.post(f'{Urls.COURIER_LOGIN}', json=courier_data)
    assert courier_login_response.status_code == 200, f"Teardown failed - не удалось залогиниться: {courier_login_response.text}"
    courier_login_response_json = courier_login_response.json()
    courier_id = courier_login_response_json["id"]
    courier_delete_response = requests.delete(f'{Urls.COURIER_DELETE}/{courier_id}')
    assert courier_delete_response.status_code == 200, f"Teardown failed - не удалось удалить курьера: {courier_delete_response.text}"
