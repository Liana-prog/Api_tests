import requests
from requests import Response


class Register:
    def __init__(self, app):
        self.app = app

    POST_REGISTER = "/register"

    def register_user(self, body: dict) -> Response:
        return requests.post(url=f"{self.app.url}{self.POST_REGISTER}", json=body)
