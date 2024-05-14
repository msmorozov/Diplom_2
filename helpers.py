from faker import Faker
import requests
import allure
from data import EndpointsUrl, ErrorMessage

@allure.step('Генерация тестовых данных российского пользователя')
def generate_user_data():
    fake = Faker('ru_RU')
    user_data = {
        "email": fake.email(),
        "password": fake.password(),
        "name": fake.first_name()
    }
    return user_data

@allure.feature('Вспомогательные функции для работы с API')

class ApiHelpersChangeData:

    @allure.step('Отправка запроса на изменение данных пользователя')
    def send_update_request(data, headers=None):
        return requests.patch(EndpointsUrl.DELETE_USER, headers=headers, json=data)

    @allure.step('Проверка успешного ответа сервера')
    def assert_response_success(response):
        assert response.status_code == 200 and response.json()['success']

    @allure.step('Проверка ответа сервера на ошибку')
    def assert_response_error(response, expected_status, expected_message=None):
        assert response.status_code == expected_status
        if expected_message:
            assert expected_message in response.text

class ApiHelpersCreateOrder:

    @allure.step("Отправка POST-запроса на URL: {url}")
    def send_order_request(url, token, data):
        return requests.post(url, headers={'Authorization': token}, json=data)

class ApiHelpersCreateUser:

    @allure.step("Отправка запроса на URL: {url}")
    def send_request(url, data):
        return requests.post(url, json=data)

    @allure.step("Проверка статуса ответа: {expected_status_code}")
    def assert_response(response, expected_status_code, expected_message=None):
        assert response.status_code == expected_status_code
        if expected_message:
            assert response.json()['message'] == expected_message

class ApiHelpersGetOrder:
    def send_get_request(token):
        return requests.get(EndpointsUrl.ORDER, headers={'Authorization': token})