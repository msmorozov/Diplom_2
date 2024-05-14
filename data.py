from mimesis import Field
class EndpointsUrl:
    BASE_URL = 'https://stellarburgers.nomoreparties.site/api'

    CREATE_USER = f'{BASE_URL}/auth/register'
    LOGIN_USER = f'{BASE_URL}/auth/login'
    DELETE_USER = f'{BASE_URL}/auth/user'
    ORDER = f'{BASE_URL}/orders'


class Ingredients:
    INGREDIENTS = {"ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa70"]}
    WITHOUT_INGREDIENTS = {"ingredients": []}
    INCORRECT_INGREDIENTS = payload = {"ingredients": ["qwertyasdfghjkl123456789", "987654321qwertyasdfghjkl"]}


class ErrorMessage:
    SERVER_ERROR = "Internal Server Error"
    NOT_AUTHORIZED = "You should be authorised"
    EXIST_USER = 'User already exists'
    INCORRECT_DATA = "email or password are incorrect"
    REQUIRED_FIELD = "Email, password and name are required fields"
    ERROR_INGREDIENT = "Ingredient ids must be provided"

class TestData:
    user_data = [
        {'email': 'new_incorrect_email@example.com', 'password': 'password123'},
        {'email': 'existing_user@example.com', 'password': 'new_incorrect_password'}
    ]

class DataUser:

    f = Field()

    EMAIL = f("email")
    PASSWORD = f("password")
    NAME = f("name")