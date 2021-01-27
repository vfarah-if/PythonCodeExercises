from utilities.date import days_ago
from pytest import fixture
from health.prescription import Prescription


@fixture
def prescription():
    "Provides a default prescription"
    return Prescription(
        description="Codeine",
        dispenseDate=days_ago(days=2),
        daysSupply=4)
