import json
import allure
import pytest
import requests
from data import Orders
from urls import Urls


@allure.feature('Создание заказа')
class TestCreateOrder:

    @pytest.mark.parametrize('order_data', [{"color": ["BLACK"]}, {"color": ["GREY"]}, {"color": [""]}, {"color": ["BLACK", "GREY"]}])
    @allure.title('Заказ может быть создан успешно')
    def test_create_order(self, order_data):
        Orders.data_order.update(order_data)
        order_data = json.dumps(Orders.data_order)
        headers = {'Content-Type': 'application/json'}
        with allure.step('Отправляем POST запрос на создание заказа'):
            response = requests.post(f'{Urls.ORDER_CREATE}', data=order_data, headers=headers)
        assert response.status_code == 201 and 'track' in response.text