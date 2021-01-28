from datetime import date, timedelta
from utilities.date import days_ago
from health.prescription import Prescription
from unittest.case import TestCase


class PrescriptionShould(TestCase):
    def setUp(self) -> None:
        self.prescription = Prescription(
            description="Codeine",
            dispenseDate=days_ago(days=2),
            daysSupply=4)

    def test_days_taken_and_exclude_future_dates(self):
        actual = list(self.prescription.days_taken())

        self.assertListEqual([days_ago(days=2), days_ago(days=1)], actual)

    def test_prescription_as_string(self):
        today = date.today()
        expected_date = today - timedelta(days=2)
        self.assertEqual(self.prescription.to_string(
        ), F"Codeine should be dispensed on the '{expected_date}' with only 4 days supply")
