import allure
import requests
from urls import Urls


@allure.title('Получение списка заказов')
class TestReturnOrderList:
    @allure.step('В тело ответа возвращается список заказов')
    def test_list_order(self):
        response = requests.get(f'{Urls.ORDER_CREATE}')
        assert response.status_code == 200 and "orders" in response.json()
