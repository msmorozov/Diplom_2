import allure
from data import EndpointsUrl, ErrorMessage
from helpers import ApiHelpersCreateUser


@allure.feature('Проверка создания пользователя')
class TestApiCreateUser:

    @allure.title('Успешное создание нового пользователя')
    def test_create_new_user_successful(self, user):
        response = ApiHelpersCreateUser.send_request(EndpointsUrl.CREATE_USER, user)
        ApiHelpersCreateUser.assert_response(response, 200)
        assert response.json()['success']

    @allure.title('Создание дубликата пользователя')
    def test_create_duplicate_user_error(self, user):
        response =ApiHelpersCreateUser.send_request(EndpointsUrl.CREATE_USER, user)
        ApiHelpersCreateUser.assert_response(response, 200)

        response_2 = ApiHelpersCreateUser.send_request(EndpointsUrl.CREATE_USER, user)
        ApiHelpersCreateUser.assert_response(response_2, 403, ErrorMessage.EXIST_USER)

    @allure.title('Ошибка при создании пользователя без обязательного параметра')
    def test_create_user_without_one_field(self, user):
        wrong_data = {"email": user["email"], "password": user["password"]}
        response = ApiHelpersCreateUser.send_request(EndpointsUrl.CREATE_USER, wrong_data)
        ApiHelpersCreateUser.assert_response(response, 403, ErrorMessage.REQUIRED_FIELD)
