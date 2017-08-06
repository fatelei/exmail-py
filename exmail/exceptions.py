# -*- coding: utf8 -*-
"""
exmail.exceptions.

~~~~~~~~~~~~~~~~~~

Exception define.
"""


class ExmailException(Exception):
    name = 'Exmail exception'

    def __init__(self, status_code, reason):
        self.status_code = status_code
        self.reason = reason

    def __str__(self):
        return '{name}({code}, {reason})'.format(
                name=self.name,
                code=self.status_code,
                reason=self.reason)


class InvalidCredential(ExmailException):
    """Invalid crop id or crop secret."""
    name = 'Invalid credential'


class ApiError(ExmailException):
    """Call api error."""
    name = 'Api error'


class ParamsError(ExmailException):
    """Params error."""
    name = 'Params error'

    def __init__(self, message):
        self._message = message

    def __str__(self):
        return '{name}({message})'.format(
                name=self.name,
                message=self._message)
