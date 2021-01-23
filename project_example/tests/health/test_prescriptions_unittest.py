from datetime import date, timedelta
from utilities.date import daysAgo
from health.prescription import Prescription
from unittest.case import TestCase


class PresciptionShould(TestCase):
    def setUp(self) -> None:
        self.prescription = Prescription(
            description="Codeine", dispenseDate=daysAgo(days=2), daysSupply=4)

    def test_days_taken_and_exclude_future_dates(self):
        actual = list(self.prescription.daysTaken())

        self.assertListEqual([daysAgo(days=2), daysAgo(days=1)], actual)

    def test_prescription_as_string(self):
        today = date.today()
        expectedDate = today - timedelta(days=2)
        self.assertEqual(self.prescription.toString(
        ), F"Codeine should be dispensed on the '{expectedDate}' with only 4 days supply")
