import requests
from requests import Response


class Auth:
    def __init__(self, app):
        self.app = app

    POST_AUTH = "/auth"

    def auth_user(self, body: dict) -> Response:
        return requests.post(url=f"{self.app.url}{self.POST_AUTH}", json=body)
