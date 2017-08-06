# -*- coding: utf8 -*-
"""
exmail.apis.sso.

~~~~~~~~~~~~~~~~

SSO api.
"""

from exmail import exceptions
from exmail.apis.base import ExmailClient
from exmail.helpers import required_params


class SSOApi(ExmailClient):
    """SSO api."""

    @required_params('userid')
    def get_login_url(self, userid=None):
        """Get login url.

        :param str userid: User's email
        :return: A login url.
        """
        if not userid:
            raise exceptions.ParamsError('userid must be set')
        
        body = {
            'access_token': self.access_token,
            'userid': userid
        }

        data = self.transport.perform_request(
            api='/login',
            body=body
        )
        return data['login_url']
