# -*- coding: utf8 -*-
"""
exmail.apis.base.

~~~~~~~~~~~~~~~~~

Base client.
"""

from exmail.auth import Auth
from exmail.transport import Transport


class ExmailClient(object):

    def __init__(self, crop_id, crop_secret, endpoint):
        """Init.

        :param str crop_id: Crop id
        :param str crop_secret: Crop secret
        :param str endpoint: Api hostname
        """
        self._auth = Auth(crop_id=crop_id,
                          crop_secret=crop_secret,
                          endpoint=endpoint)
        self._transport = Transport(endpoint=endpoint)

    @property
    def transport(self):
        return self._transport

    @property
    def access_token(self):
        return self._auth.access_token
