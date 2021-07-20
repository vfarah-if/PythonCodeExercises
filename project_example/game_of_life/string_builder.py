from os import linesep as eol

from io import StringIO


class StringBuilder:
    """Optimised way of concatenating immutable strings"""
    _logger = None

    def __init__(self, value=None):
        self._logger = StringIO()
        if value is not None:
            self.add(value)

    def add(self, value):
        self._logger.write(value)
        return self

    def newline(self):
        self.add(eol)
        return self

    def to_string(self):
        return str(self)

    def __str__(self):
        return self._logger.getvalue()
