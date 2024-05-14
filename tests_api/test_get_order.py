import allure
from helpers import ApiHelpersGetOrder
from data import ErrorMessage

@allure.feature('Проверяем получение заказа пользователя')
class TestApiGetUserOrders:

    @allure.title('Получение заказа авторизованного пользователя')
    def test_auth_user_get_order_successful(self, token_create_and_delete_fixture):
        response = ApiHelpersGetOrder.send_get_request(token_create_and_delete_fixture)
        assert response.status_code == 200 and response.json().get('success')

    @allure.title('Получение заказа пользователя без авторизации')
    def test_no_auth_user_get_user_order_error(self):
        response = ApiHelpersGetOrder.send_get_request(None)
        assert response.status_code == 401
        assert ErrorMessage.NOT_AUTHORIZED in response.text