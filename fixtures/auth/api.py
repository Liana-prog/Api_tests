import requests
from requests import Response

from fixtures.register.model import RegisterObj


class Auth:
    def __init__(self, app):
        self.app = app

    POST_AUTH = "/auth"

    def auth_user(self, body: RegisterObj) -> Response:
        return self.app.client.request('POST', url=f"{self.app.url}{self.POST_AUTH}", json=body.to_dict())
