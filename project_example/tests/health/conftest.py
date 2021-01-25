from utilities.date import daysAgo
from pytest import fixture
from health.prescription import Prescription


@fixture
def prescription():
    "Provides a default prescription"
    return Prescription(
        description="Codeine",
        dispenseDate=daysAgo(days=2),
        daysSupply=4)
