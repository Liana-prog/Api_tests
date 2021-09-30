import pytest

from fixtures.app import App


@pytest.fixture
def app(request):
    url = request.config.getoption('--api-url')
    return App(url)


def pytest_addoption(parser):
    parser.addoption(
        "--api-url",
        action="store",
        help="enter api url",
        default="https://stores-tests-api.herokuapp.com",
    )