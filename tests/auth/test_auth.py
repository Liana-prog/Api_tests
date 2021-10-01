import requests
from faker import Faker

from fixtures import app
from fixtures.register.model import RegisterObj

BASE_URL = "https://stores-tests-api.herokuapp.com"
fake = Faker()


class TestAuth:
    def test_auth_valid_data(self, app):
        """
        1. Try to auth with valid data
        2. Check that status code is 200
        3. Check response
       """
        body_old = {'username': fake.email(), 'password': fake.password()}
        body = RegisterObj.random()
        res = app.register.register_user(body)
        assert res.status_code == 201
        assert res.json().get('message') == 'User created successfully.'
        res2 = app.auth.auth_user(body)
        assert res2.status_code == 200


        # # Register new user
        # body = {'username': fake.email(), 'password': fake.password()}
        # response1 = requests.post(url=f'{BASE_URL}/register', json=body)
        # assert response1.status_code == 201
        # assert response1.json().get('message') == 'User created successfully.'
        # # Auth user
        # response2 = requests.post(url=f'{BASE_URL}/auth', json=body)
        # assert response2.status_code == 200


    def test_auth_invalid_data(self, app):
        """
        1. Try to auth with invalid data
        2. Check that status code is 401; error='Bad request'; description='Invalid credentials'
        3. Check response
        """
        body = {'username': fake.email(), 'password': fake.password()}
        res = app.auth.auth_user(body)
        assert res.status_code == 401
        assert res.json().get('error') == 'Bad Request'
        assert res.json().get('description') == 'Invalid credentials'


        # body1 = {'username': fake.email(), 'password': fake.password()}
        # response2 = requests.post(url=f'{BASE_URL}/auth', json=body1)
        # assert response2.status_code == 401
        # assert response2.json().get('error') == 'Bad Request'
        # assert response2.json().get('description') == 'Invalid credentials'
