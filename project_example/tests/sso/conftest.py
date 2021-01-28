from pytest import fixture
from sso.my_service import MyService


@fixture
def my_service():
    "Provides a default Service"
    return MyService(None)
