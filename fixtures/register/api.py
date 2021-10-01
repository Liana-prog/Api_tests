from requests import Response

from fixtures.register.model import RegisterObj


class Register:
    def __init__(self, app):
        self.app = app

    POST_REGISTER = "/register"

    def register_user(self, body: RegisterObj) -> Response:
        return self.app.client.\
            request('POST', url=f"{self.app.url}{self.POST_REGISTER}", json=body.to_dict())
