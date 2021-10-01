from fixtures.auth.api import Auth
from fixtures.register.api import Register
from fixtures.requests import Client


class App:
    def __init__(self, url):
        self.url = url
        self.client = Client
        self.register = Register(self)
        self.auth = Auth(self)
