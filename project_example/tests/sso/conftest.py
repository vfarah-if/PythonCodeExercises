from pytest import fixture
from sso.my_service import MyService

@fixture
def myService():
    "Provides a default Service"
    return MyService(None)
