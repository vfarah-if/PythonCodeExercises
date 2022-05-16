import io
import sys

from decorators.printer import printer, handler


def test_passing_arguments_to_decorators():
    actualOutput = io.StringIO()          # Create StringIO object
    sys.stdout = actualOutput

    actual = printer(1, 2)

    assert actualOutput.getvalue() == 'before function\nin function\nafter function\n'
    assert actual == 3


def test_task_execution_of_handler():
    actualOutput = io.StringIO()          # Create StringIO object
    sys.stdout = actualOutput

    actual = handler(1, 2)

    assert actualOutput.getvalue() == "Before running task (1, 2) {} True 9 short-running\nRunning task 1 2\nAfter running task 3\n"
    assert actual == 3
