from datetime import date
from utilities.date import daysAgo
from health.prescription import Prescription
from unittest.case import TestCase


class DaysAgoShould(TestCase):
    def test_date_generated_represented(self):
        dayCount = 2
        actual = daysAgo(dayCount)
        today = date.today()

        self.assertEqual(actual.day, today.day - dayCount)
        self.assertEqual(actual.month, today.month)
        self.assertEqual(actual.year, today.year)


class PresciptionShould(TestCase):
    def setUp(self) -> None:
        self.prescription = Prescription(
            description="Codeine", dispenseDate=daysAgo(days=2), daysSupply=4)

    def test_days_taken_exclude_future_dates(self):
        actual = list(self.prescription.daysTaken())

        self.assertListEqual([daysAgo(days=2), daysAgo(days=1)], actual)

    def test_prescription_as_string(self):
        self.assertEqual(self.prescription.toString(
        ), "Codeine should be dispensed on the '2021-01-21' with only 4 days supply")
