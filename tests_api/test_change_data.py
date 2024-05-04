import allure
from helpers import ApiHelpersChangeData
from data import ErrorMessage


@allure.feature('Изменение данных пользователя')
class TestApiUpdateUserData:

    @allure.title('Изменение данных авторизованного пользователя')
    def test_update_authorized_user(self, token):
        user_token = token
        new_name = 'Maxim'
        data = {"name": new_name}

        with allure.step('Отправка запроса на изменение данных пользователя'):
            response = ApiHelpersChangeData.send_update_request(data, headers={'Authorization': user_token})

        with allure.step('Проверка успешного ответа сервера'):
            ApiHelpersChangeData.assert_response_success(response)

    @allure.title('Изменение данных неавторизованного пользователя')
    def test_update_unauthorized_user(self, user):
        data = user

        with allure.step('Отправка запроса на изменение данных пользователя'):
            response = ApiHelpersChangeData.send_update_request(data)

        with allure.step('Проверка ответа сервера на ошибку'):
            ApiHelpersChangeData.assert_response_error(response, 401, ErrorMessage.NOT_AUTHORIZED)
