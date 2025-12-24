import json
import allure
import pytest
import requests
from data import Orders
from urls import Urls


@allure.title('Создание заказа')
class TestCreateOrder:

    @pytest.mark.parametrize('order_data', [{"color": ["BLACK"]}, {"color": ["GREY"]}, {"color": [""]}, {"color": ["BLACK", "GREY"]}])
    @allure.step('Заказ может быть создан успешно')
    def test_create_order(self, order_data):
        Orders.data_order.update(order_data)
        order_data = json.dumps(Orders.data_order)
        headers = {'Content-Type': 'application/json'}
        response = requests.post(f'{Urls.ORDER_CREATE}', data=order_data, headers=headers)
        assert response.status_code == 201 and 'track' in response.text