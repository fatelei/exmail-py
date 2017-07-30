# -*- coding: utf8 -*-
"""
exmail.auth.

~~~~~~~~~~~~

Get access token by crop id and secret.
"""

import time


class Auth(object):
    """Get access token by crop id and secret."""

    def __init__(self, crop_id, crop_secret, endpoint):
        """Init.

        :param str crop_id: Crop id
        :param str crop_secret: Crop secret
        """
        self.crop_id = crop_id
        self.crop_secret = crop_secret
        self.endpoint = endpoint
        self._access_token = None
        self._expire_at = None

    @property
    def access_token(self):
        """Request access token."""
        now = int(time.time())
        if not self._access_token or now > self._expire_at:
            # Request a new access token.
            pass
        return self._access_token
