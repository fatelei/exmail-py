# -*- coding: utf8 -*-
"""
tests.test_auth.

~~~~~~~~~~~~~~~~~~~

Unittest for `exmail.auth.Auth`.
"""

import pytest

from exmail.auth import Auth


class AuthResponse(object):

    def __init__(self):
        self.status = 200
        self.data = '{"access_token": 1, "expires_in": 1504005038}'


class TestAuth(object):

    @pytest.fixture(autouse=True)
    def test_access_token(self, monkeypatch):
        def authresponse(*args, **kwargs):
            return AuthResponse()

        auth = Auth('a', 'b', 'http://localhost')
        monkeypatch.setattr(auth._transport.http_pool, 'request', authresponse)
        assert auth.access_token == 1
