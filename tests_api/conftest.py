import pytest
import requests
import helpers
from data import EndpointsUrl
from faker import Faker


@pytest.fixture(scope="function")
def user_create_fixture():
    """
    Фикстура для создания пользователя перед тестом.
    """
    user_data = helpers.generate_user_data()
    yield user_data

@pytest.fixture
def token_create_and_delete_fixture():
    """
    Фикстура для создания токена доступа перед тестом и его удаления после теста.
    """
    fake = Faker('ru_RU')
    user_data = {
        "email": fake.email(),
        "password": fake.password(),
        "name": fake.first_name()
    }
    response = requests.post(EndpointsUrl.CREATE_USER, json=user_data)
    token = response.json().get("accessToken")

    yield token
    requests.delete(EndpointsUrl.DELETE_USER, headers={'Authorization': token})
