import allure
from data import EndpointsUrl, Ingredients, ErrorMessage
from helpers import ApiHelpersCreateOrder

@allure.feature('Проверяем создание заказа')
class TestApiCreateOrder:

    @allure.title('Тест успешного создания заказа авторизованным пользователем')
    def test_auth_user_create_order_successful(self, token_create_and_delete_fixture):
        response = ApiHelpersCreateOrder.send_order_request(EndpointsUrl.ORDER, token_create_and_delete_fixture, Ingredients.INGREDIENTS)
        assert response.status_code == 200 and response.json()['success']

    @allure.title('Тест успешного создания заказа неавторизованным пользователем')
    def test_create_order_with_ingredients_user_no_auth_successful(self):
        response = ApiHelpersCreateOrder.send_order_request(EndpointsUrl.ORDER, None, Ingredients.INGREDIENTS)
        assert response.status_code == 200 and response.json()['success']

    @allure.title('Тест ошибки создания заказа без ингредиентов')
    def test_create_order_without_ingredients_error(self):
        response = ApiHelpersCreateOrder.send_order_request(EndpointsUrl.ORDER, None, Ingredients.WITHOUT_INGREDIENTS)
        assert response.status_code == 400 and response.json()['message'] == ErrorMessage.ERROR_INGREDIENT

    @allure.title('Тест ошибки создания заказа с неправильными ингредиентами')
    def test_create_order_bad_ingredients_error(self):
        response = ApiHelpersCreateOrder.send_order_request(EndpointsUrl.ORDER, None, Ingredients.INCORRECT_INGREDIENTS)
        assert response.status_code == 500 and ErrorMessage.SERVER_ERROR in response.text
