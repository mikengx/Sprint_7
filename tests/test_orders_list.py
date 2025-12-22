import allure
import requests
from urls import Urls


class TestReturnOrderList:
    @allure.title('В тело ответа возвращается список заказов')
    def test_list_order(self):
        response = requests.get(f'{Urls.ORDER_CREATE}')
        assert response.status_code == 200 and "orders" in response.json()
