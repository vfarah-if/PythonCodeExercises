import io
import sys

from decorators.printer import printer


def test_passing_arguments_to_decorators():
    actualOutput = io.StringIO()          # Create StringIO object
    sys.stdout = actualOutput

    actual = printer(1, 2)

    assert actualOutput.getvalue() == 'before function\nin function\nafter function\n'
    assert actual == 3
