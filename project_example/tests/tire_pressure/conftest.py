from pytest import fixture
from tire_pressure.alarm import Alarm


@fixture
def alarm():
    "Provides a default alarm"
    return Alarm()
