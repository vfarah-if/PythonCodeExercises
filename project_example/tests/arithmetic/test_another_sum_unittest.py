from arithmetic.another_sum import another_sum
from unittest.case import TestCase


class AnotherSumShould(TestCase):
    def test_add_two_values(self):
        self.assertEqual(another_sum(3, 5), 8)
