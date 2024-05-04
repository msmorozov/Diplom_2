import allure
import requests
from data import EndpointsUrl, ErrorMessage, TestData

@allure.feature('Проверяем авторизацию пользователя')
class TestLoginUser:

    @staticmethod
    @allure.title('Тест авторизации существующего пользователя')
    def test_login_existing_user(user):
        assert requests.post(EndpointsUrl.CREATE_USER, json=user).json().get('success')
        assert requests.post(EndpointsUrl.LOGIN_USER, json=user).json().get('success')

    @staticmethod
    @allure.title('Тест авторизации с неверными учетными данными')
    def test_login_user_incorrect_credentials():
        for data in TestData.user_data:
            response = requests.post(EndpointsUrl.LOGIN_USER, json=data)
            assert response.status_code == 401 and response.json().get('message') == ErrorMessage.INCORRECT_DATA
