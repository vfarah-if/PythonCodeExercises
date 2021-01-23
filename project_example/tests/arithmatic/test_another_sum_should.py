import pytest

from arithmatic.another_sum import another_sum

def test_add_two_values():
    assert another_sum(3, 2) == 5
