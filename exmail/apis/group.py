# -*- coding: utf8 -*-
"""
exmail.apis.group.

~~~~~~~~~~~~~~~~~~

Email group apis.
"""

from exmail import exceptions
from exmail.apis.base import ExmailClient
from exmail.helpers import required_params


class GroupApi(ExmailClient):

    @required_params('groupid', 'groupname', 'allow_type')
    def create_group(self,
                     groupid=None,
                     groupname=None,
                     userlist=None,
                     grouplist=None,
                     departments=None,
                     allow_type=0,
                     allow_userlist=None):
        """Create a mail group.

        :param str groupid: Group email address
        :param str groupname: Group email name
        :param tuple userlist: Users in group
        :param tuple grouplist: Groups
        :param tuple departments: Departments
        :param int allow_type: The permission of send group mail
        :param tuple allow_userlist: The user who have permission to send group mail
        """
        if not groupid and \
           not groupname:
            raise exceptions.ParamsError('groupid and groupname should be set')

        if not userlist and \
           not grouplist and \
           not departments:
            raise exceptions.ParamsError(
                'userlist, grouplist and departments must be set at one least')

        body = {
            'groupid': groupid,
            'groupname': groupname,
            'allow_type': allow_type,
        }

        if userlist and isinstance(userlist, tuple):
            body['userlist'] = userlist

        if grouplist and isinstance(grouplist, tuple):
            body['grouplist'] = grouplist

        if departments and isinstance(departments, tuple):
            body['department'] = departments

        if allow_userlist and isinstance(allow_userlist, tuple):
            body['allow_userlist'] = allow_userlist

        self.transport.perform_request(
            api='/group/create?access_token=%s' % self.access_token,
            body=body,
            method='POST'
        )

    @required_params('groupid')
    def update_group(self,
                     groupid=None,
                     groupname=None,
                     userlist=None,
                     grouplist=None,
                     departments=None,
                     allow_type=0,
                     allow_userlist=None):
        """Update a mail group.

        :param str groupid: Group email address
        :param str groupname: Group email name
        :param tuple userlist: Users in group
        :param tuple grouplist: Groups
        :param tuple departments: Departments
        :param int allow_type: The permission of send group mail
        :param tuple allow_userlist: The user who have permission to send group mail
        """
        if not groupid:
            raise exceptions.ParamsError('groupid should be set')

        body = {
            'groupid': groupid
        }

        if groupname:
            body['groupname'] = groupname
        
        if userlist and isinstance(userlist, tuple):
            body['userlist'] = userlist

        if grouplist and isinstance(grouplist, tuple):
            body['grouplist'] = grouplist

        if departments and isinstance(departments, tuple):
            body['department'] = departments

        if allow_userlist and isinstance(allow_userlist, tuple):
            body['allow_userlist'] = allow_userlist

        if len(body.keys()) == 1:
            return

        self.transport.perform_request(
            api='/group/update?access_token=%s' % self.access_token,
            body=body,
            method='POST'
        )

    @required_params('groupid')
    def delete_group(self,
                     groupid=None):
        """Delete a mail group.

        :param str groupid: Group email address
        """
        if not groupid:
            raise exceptions.ParamsError('groupid should be set')

        body = {
            'groupid': groupid,
            'access_token': self.access_token
        }

        self.transport.perform_request(
            api='/group/delete',
            body=body
        )

    @required_params('groupid')
    def get_group(self,
                  groupid=None):
        """Get a mail group info.

        :param str groupid: Group email address
        :return: A dict
        """
        if not groupid:
            raise exceptions.ParamsError('groupid should be set')

        body = {
            'groupid': groupid,
            'access_token': self.access_token
        }

        return self.transport.perform_request(
            api='/group/get',
            body=body
        )