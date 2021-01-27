from datetime import date, timedelta
from utilities.date import days_ago


def test_days_taken_and_exclude_future_dates(prescription):
    actual = list(prescription.days_taken())

    assert [days_ago(days=2), days_ago(days=1)] == actual


def test_prescription_as_string(prescription):
    today = date.today()
    expectedDate = today - timedelta(days=2)
    
    actual = prescription.to_string()
    assert actual == F"Codeine should be dispensed on the '{expectedDate}' with only 4 days supply"

