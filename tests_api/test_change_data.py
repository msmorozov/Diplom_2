import allure
import pytest
from helpers import ApiHelpersChangeData
from data import ErrorMessage, DataUser


@allure.feature('Изменение данных пользователя')
class TestApiUpdateUserData:

    @allure.title('Изменение данных авторизованного пользователя')
    @pytest.mark.parametrize(
        'new_name, new_mail, new_password',
        [(DataUser.NAME, None, None),
         (None, DataUser.EMAIL, None),
         (None, None, DataUser.PASSWORD)]
    )
    def test_update_authorized_user(self, token_create_and_delete_fixture,new_name, new_mail, new_password):
        user_token = token_create_and_delete_fixture
        data = {"name": new_name, "mail": new_mail, "password": new_password}

        response = ApiHelpersChangeData.send_update_request(data, headers={'Authorization': user_token})
        ApiHelpersChangeData.assert_response_success(response)

    @allure.title('Изменение данных неавторизованного пользователя')
    @pytest.mark.parametrize(
        'new_name, new_mail, new_password',
        [(DataUser.NAME, None, None),
         (None, DataUser.EMAIL, None),
         (None, None, DataUser.PASSWORD)]
    )
    def test_update_unauthorized_user(self, user_create_fixture, new_name, new_mail, new_password):
        data = {"name": new_name, "mail": new_mail, "password": new_password}

        response = ApiHelpersChangeData.send_update_request(data)
        ApiHelpersChangeData.assert_response_error(response, 401, ErrorMessage.NOT_AUTHORIZED)