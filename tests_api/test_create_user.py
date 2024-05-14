import allure
from data import EndpointsUrl, ErrorMessage
from helpers import ApiHelpersCreateUser


@allure.feature('Проверка создания пользователя')
class TestApiCreateUser:

    @allure.title('Успешное создание нового пользователя')
    def test_create_new_user_successful(self, user_create_fixture):
        response = ApiHelpersCreateUser.send_request(EndpointsUrl.CREATE_USER, user_create_fixture)
        ApiHelpersCreateUser.assert_response(response, 200)
        assert response.json()['success']

    @allure.title('Ошибка при создании дубликата пользователя')
    def test_create_duplicate_user_error(self, user_create_fixture):
        # Сначала создаем пользователя
        ApiHelpersCreateUser.send_request(EndpointsUrl.CREATE_USER, user_create_fixture)
        # Пытаемся создать дубликат и проверяем ошибку
        response_2 = ApiHelpersCreateUser.send_request(EndpointsUrl.CREATE_USER, user_create_fixture)
        ApiHelpersCreateUser.assert_response(response_2, 403, ErrorMessage.EXIST_USER)

    @allure.title('Ошибка при создании пользователя без обязательного параметра')
    def test_create_user_without_one_field(self, user_create_fixture):
        wrong_data = {"email": user_create_fixture["email"], "password": user_create_fixture["password"]}
        response = ApiHelpersCreateUser.send_request(EndpointsUrl.CREATE_USER, wrong_data)
        ApiHelpersCreateUser.assert_response(response, 403, ErrorMessage.REQUIRED_FIELD)
