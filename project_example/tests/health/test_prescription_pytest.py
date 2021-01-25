from datetime import date, timedelta
from utilities.date import daysAgo


def test_days_taken_and_exclude_future_dates(prescription):
    actual = list(prescription.daysTaken())

    assert [daysAgo(days=2), daysAgo(days=1)] == actual


def test_prescription_as_string(prescription):
    today = date.today()
    expectedDate = today - timedelta(days=2)
    
    actual = prescription.toString() 
    assert actual == F"Codeine should be dispensed on the '{expectedDate}' with only 4 days supply"

