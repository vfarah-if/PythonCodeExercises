from datetime import date
from unittest.case import TestCase
from utilities.date import days_ago


class DaysAgoShould(TestCase):
    def test_date_generated_is_correct(self):
        day_count = 2
        today = date.today()

        actual = days_ago(day_count)

        self.assertEqual(actual.day, today.day - day_count)
        self.assertEqual(actual.month, today.month)
        self.assertEqual(actual.year, today.year)
