# -*- coding: utf8 -*-
"""
exmail.apis.contact.

~~~~~~~~~~~~~~~~~~~~~~~

Contact apis.
"""

from exmail import exceptions
from exmail.apis.base import ExmailClient
from exmail.helpers import required_params


class UserApi(ExmailClient):
    """Contact apis."""

    @required_params('userid', 'name', 'department', 'password')
    def create_user(self,
                    userid=None,
                    name=None,
                    department=[],
                    position=None,
                    mobile=None,
                    tel=None,
                    extid=None,
                    gender=None,
                    slaves=[],
                    password=None,
                    cpwd_login=0):
        """Create a new user.

        :param str userid: User's email
        :param str name: User's name
        :param list department: User's department lists
        :param str position Position name
        :param str mobile: Mobile phone number
        :param str tel: Telephone number
        :param str extid:
        :param int gender: 1 is man, 2 is woman
        :param list slaves: Alias
        :param str password: Login password
        :param int cpwd_login: Change password after login
        """
        if len(department) > 20:
            raise exceptions.ParamsError('Departments must be within 20')
        
        if not isinstance(department, tuple):
            raise exceptions.ParamsError('department should be tuple type')

        if len(slaves) > 5:
            raise exceptions.ParamsError('Slaves must be within 5')

        if slaves and not isinstance(slaves, tuple):
            raise exceptions.ParamsError('slaves should be tuple type')

        body = {
            'userid': userid,
            'name': name,
            'department': department,
            'position': position,
            'mobile': mobile,
            'tel': tel,
            'extid': extid,
            'gender': gender,
            'slaves': slaves,
            'password': password,
            'cpwd_login': cpwd_login
        }

        self.transport.perform_request(
            api='/user/create?access_token=%s' % self.access_token, 
            body=body,
            method='POST'
        )

    @required_params('userid')
    def update_user(self,
                    userid=None,
                    name=None,
                    department=[],
                    position=None,
                    mobile=None,
                    tel=None,
                    extid=None,
                    gender=None,
                    slaves=[],
                    password=None,
                    cpwd_login=0):
        """Update a new user.

        :param str userid: User's email
        :param str name: User's name
        :param list department: User's department lists
        :param str position Position name
        :param str mobile: Mobile phone number
        :param str tel: Telephone number
        :param str extid:
        :param int gender: 1 is man, 2 is woman
        :param list slaves: Alias
        :param str password: Login password
        :param int cpwd_login: Change password after login
        """
        if len(department) > 20:
            raise exceptions.ParamsError('Departments must be within 20')
        
        if department and not isinstance(department, tuple):
            raise exceptions.ParamsError('department should be tuple type')

        if len(slaves) > 5:
            raise exceptions.ParamsError('Slaves must be within 5')

        if slaves and not isinstance(slaves, tuple):
            raise exceptions.ParamsError('slaves should be tuple type')

        body = {
            'userid': userid,
            'name': name,
            'department': department,
            'position': position,
            'mobile': mobile,
            'tel': tel,
            'extid': extid,
            'gender': gender,
            'slaves': slaves,
            'password': password,
            'cpwd_login': cpwd_login
        }

        self.transport.perform_request(
            api='/user/update?access_token=%s' % self.access_token, 
            body=body,
            method='POST'
        )

    @required_params('userid')
    def delete_user(self,
                    userid=None):
        """Delete a user.

        :param str userid: User's email
        """
        if not userid:
            raise exceptions.ParamsError('userid should be set')

        self.transport.perform_request(
            api='/user/delete', 
            body={'userid': userid, 'access_token': self.access_token}
        )

    @required_params('userid')
    def get_user(self,
                 userid=None):
        """Get a user.

        :param str userid: User's email
        """
        if not userid:
            raise exceptions.ParamsError('userid should be set')

        data = self.transport.perform_request(
            api='/user/get', 
            body={'userid': userid, 'access_token': self.access_token}
        )
        return data

    @required_params('userlist')
    def check_users(self, userlist=[]):
        """Check user is valid or not.

        :param list userlist: A list of user's email
        :return: Check results.
        """
        if not userlist:
            return []

        data = self.transport.perform_request(
            api='/user/batchcheck?access_token=%s' % self.access_token,
            body={'userlist': userlist},
            method='POST'
        )
        return data['list']

    @required_params('department_id')
    def list_users(self, department_id=None, is_simple=True):
        """Get users of a department.

        :param int department_id: Department id
        :param bool is_simple: Result is simple or not
        :return: A list of users.
        """
        if not department_id:
            return []
    
        if is_simple:
            api = '/user/simplelist'
        else:
            api = '/user/list'

        body = {
            'access_token': self.access_token,
            'department_id': department_id,
        }

        data = self.transport.perform_request(
            api=api,
            body=body
        )
        return data['userlist']
