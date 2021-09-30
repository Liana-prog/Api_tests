from fixtures.auth.api import Auth
from fixtures.register.api import Register


class App:
    def __init__(self, url):
        self.url = url
        self.register = Register(self)
        self.auth = Auth(self)
