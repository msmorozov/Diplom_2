import pytest
import requests
import helpers
from data import EndpointsUrl


@pytest.fixture(scope="function")
def user():
    user_data = helpers.generate_user_data()

    yield user_data

    data = {
        "email": user_data["email"],
        "password": user_data["password"],
    }
    response = requests.post(EndpointsUrl.LOGIN_USER, json=data)
    token = response.json().get("accessToken")

    if token:
        requests.delete(EndpointsUrl.DELETE_USER, headers={'Authorization': token})


@pytest.fixture
def token():
    data = helpers.generate_user_data()
    response = requests.post(EndpointsUrl.CREATE_USER, json=data)
    token = response.json().get("accessToken")

    yield token
    requests.delete(EndpointsUrl.DELETE_USER, headers={'Authorization': token})

