import requests
from faker import Faker

from fixtures import app

BASE_URL = "https://stores-tests-api.herokuapp.com"
fake = Faker()


class TestRegister:
    def test_register_valid_data(self, app):

        """
        1. Try to register with valid data
        2. Check that status code is 201
        3. Check response
        """

        body = {'username': fake.email(), 'password': fake.password()}
        res = app.register.register_user(body)
        assert res.status_code == 201
        assert res.json().get('message') == 'User created successfully.'


        # body = {'username': fake.email(), 'password': fake.password()}
        # response1 = requests.post(url=f'{BASE_URL}/register', json=body)
        # assert response1.status_code == 201
        # assert response1.json().get('message') == 'User created successfully.'

    def test_register_invalid_data_1(self, app):

        """
        1. Try to register with old data
        2. Check that status code is 400
        3. Check response
        """

        body = {'username': fake.email(), 'password': fake.password()}
        res = app.register.register_user(body)
        assert res.status_code == 201
        assert res.json().get('message') == 'User created successfully.'
        res2 = app.register.register_user(body)
        assert res2.status_code == 400
        assert res2.json().get('message') == 'A user with that username already exists'

        # body = {'username': fake.email(), 'password': fake.password()}
        # response1 = requests.post(url=f'{BASE_URL}/register', json=body)
        # assert response1.status_code == 201
        # assert response1.json().get('message') == 'User created successfully.'
        # response2 = requests.post(url=f'{BASE_URL}/register', json=body)
        # assert response2.status_code == 400
        # assert response2.json().get('message') == 'A user with that username already exists'

    def test_register_invalid_data_2(self, app):

        """
        1. Try to register with empty data
        2. Check that status code is 400
        3. Check response
        # """

        body = {'username': None, 'password': fake.password()}
        res = app.register.register_user(body)
        assert res.status_code == 400
        assert res.json().get('message') == 'Username and password are required fields'

        # body1 = {'username': None,'password': fake.password()}
        # response3 = requests.post(url=f'{BASE_URL}/register', json=body1)
        # assert response3.status_code == 400
        # assert response3.json().get('message') == 'Username and password are required fields'