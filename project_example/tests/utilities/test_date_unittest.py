from datetime import date
from unittest.case import TestCase
from utilities.date import daysAgo

class DaysAgoShould(TestCase):
    def test_date_generated_is_correct(self):
        dayCount = 2        
        today = date.today()

        actual = daysAgo(dayCount)
        
        self.assertEqual(actual.day, today.day - dayCount)
        self.assertEqual(actual.month, today.month)
        self.assertEqual(actual.year, today.year)
