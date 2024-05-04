import allure
from data import EndpointsUrl, Ingredients, ErrorMessage
from helpers import ApiHelpersCreateOrder

@allure.feature('Проверяем создание заказа')
class TestApiCreateOrder:

    def test_auth_user_create_order_successful(self, token):
        response = ApiHelpersCreateOrder.send_order_request(EndpointsUrl.ORDER, token, Ingredients.INGREDIENTS)
        assert response.status_code == 200 and response.json()['success']

    def test_create_order_with_ingredients_user_no_auth_successful(self):
        response = ApiHelpersCreateOrder.send_order_request(EndpointsUrl.ORDER, None, Ingredients.INGREDIENTS)
        assert response.status_code == 200 and response.json()['success']

    def test_create_order_without_ingredients_error(self):
        response = ApiHelpersCreateOrder.send_order_request(EndpointsUrl.ORDER, None, Ingredients.WITHOUT_INGREDIENTS)
        assert response.status_code == 400 and response.json()['message'] == ErrorMessage.ERROR_INGREDIENT

    def test_create_order_bad_ingredients_error(self):
        response = ApiHelpersCreateOrder.send_order_request(EndpointsUrl.ORDER, None, Ingredients.INCORRECT_INGREDIENTS)
        assert response.status_code == 500 and ErrorMessage.SERVER_ERROR in response.text
