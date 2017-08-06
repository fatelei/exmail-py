# -*- coding: utf8 -*-
"""
exmail.auth.

~~~~~~~~~~~~

Get access token by crop id and secret.
"""

import time

from exmail.transport import Transport


class Auth(object):
    """Get access token by crop id and secret."""

    def __init__(self, crop_id, crop_secret, endpoint):
        """Init.

        :param str crop_id: Crop id
        :param str crop_secret: Crop secret
        :param str endpoint: Api hostname
        """
        self.crop_id = crop_id
        self.crop_secret = crop_secret
        self.endpoint = endpoint
        self._access_token = None
        self._expire_at = None
        self._transport = Transport(endpoint=endpoint)
        self._api = '/gettoken'

    @property
    def access_token(self):
        """Request access token."""
        now = int(time.time())
        if not self._access_token or now > self._expire_at:
            # Request a new access token.
            data = self._transport.perform_request(
                api=self._api,
                body={'corpid': self.crop_id, 'corpsecret': self.crop_secret})
            self._access_token = data['access_token']
            self._expire_at = now + data['expires_in']
        return self._access_token
