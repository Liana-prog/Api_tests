from faker import Faker

from fixtures.base import BaseClass

fake = Faker()


class RegisterObj(BaseClass):
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @staticmethod
    def random():
        username = fake.email()
        password = fake.password()
        return RegisterObj(username=username, password=password)


