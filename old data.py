body1 = {'username': fake.email(), 'password': fake.password()}
response2 = requests.post(url=f'{BASE_URL}/auth', json=body1)
assert response2.status_code == 401
assert response2.json().get('error') == 'Bad Request'
assert response2.json().get('description') == 'Invalid credentials'