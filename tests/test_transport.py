# -*- coding: utf8 -*-
"""
tests.test_transport.

~~~~~~~~~~~~~~~~~~~~~

Unittest for `exmail.transport.Transport`.
"""

import pytest

from exmail.transport import Transport
from exmail.exceptions import ExmailException
from exmail.exceptions import ApiError


class Response5xx(object):

    def __init__(self):
        self.status = 500
        self.data = '500'


class Response4xx(object):

    def __init__(self):
        self.status = 400
        self.data = '500'


class Response2xx(object):

    def __init__(self):
        self.status = 200
        self.data = '{"errcode": 1, "errmsg": "233"}'


class TestTransport(object):

    def test_make_path(self):
        ts = Transport(endpoint='http://localhost')
        target = 'http://localhost/cgi-bin/a'
        assert ts._make_path('/a') == target

    @pytest.fixture(autouse=True)
    def test_perform_5xx_request(self, monkeypatch):
        def mock5xxreturn(*args, **kwargs):
            return Response5xx()

        ts = Transport(endpoint='http://localhost')
        monkeypatch.setattr(ts.http_pool, 'request', mock5xxreturn)

        with pytest.raises(ExmailException):
            ts.perform_request(api='/a', body={'a': 1}, method='GET')

    @pytest.fixture(autouse=True)
    def test_perform_4xx_request(self, monkeypatch):
        def mock4xxreturn(*args, **kwargs):
            return Response4xx()

        ts = Transport(endpoint='http://localhost')
        monkeypatch.setattr(ts.http_pool, 'request', mock4xxreturn)

        with pytest.raises(ApiError):
            ts.perform_request(api='/a', body={'a': 1}, method='GET')

    @pytest.fixture(autouse=True)
    def test_perform_2xx_request(self, monkeypatch):
        def mock2xxreturn(*args, **kwargs):
            return Response2xx()

        ts = Transport(endpoint='http://localhost')
        monkeypatch.setattr(ts.http_pool, 'request', mock2xxreturn)
        with pytest.raises(ApiError):
            ts.perform_request(api='/a', body={'a': 1}, method='GET')
