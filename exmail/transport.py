# -*- coding: utf8 -*-
"""
exmail.transport.

~~~~~~~~~~~~~~~~~

Implement transport between api servers and clinet.
"""

import functools
import json
import logging
import urllib3

from exmail import exceptions


class Transport(object):
    """Implement transport between api servers and clinet."""

    def __init__(self, endpoint):
        """Init.

        :param str endpoint: Api endpoint
        """
        self.endpoint = endpoint
        self.http_pool = urllib3.PoolManager()

    def _make_path(self, api):
        """Make request url."""
        return '%s/cgi-bin%s' % (self.endpoint, api)

    def perform_request(self, api, body, method='GET'):
        """Perform request.

        :param str api: Api path
        :param dict body: Request body
        :param str method: HTTP method
        :return: HTTP response
        :raise: ConnectTimeoutError
        """
        url = self._make_path(api)
        func = functools.partial(self.http_pool.request, method, url)
        if method == 'GET':
            resp = func(fields=body)
        else:
            body = json.dumps(body).encode('utf8')
            resp = func(
                body=body,
                headers={'Content-Type': 'application/json'}
            )

        status, data = resp.status, resp.data
        if status >= 500:
            raise exceptions.ExmailException(status, data)
        elif 400 <= status < 500:
            raise exceptions.ApiError(status, data)

        data = json.loads(data.decode('utf8'))
        errcode, errmsg = data.pop('errcode'), data.pop('errmsg')
        if errcode != 0:
            raise exceptions.ApiError(errcode, errmsg)
        logging.debug('Call api {} return ({}, {})'.format(
            api, errcode, errmsg))
        return data
