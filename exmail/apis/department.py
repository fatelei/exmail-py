# -*- coding: utf8 -*-
"""
exmail.apis.department.

~~~~~~~~~~~~~~~~~~~~~~~

Department apis.
"""

from exmail import exceptions
from exmail.apis.base import ExmailClient
from exmail.helpers import required_params


class DepartmentApi(ExmailClient):

    @required_params('name', 'parentid')
    def create_department(self, name=None, parentid=None, order=None):
        """Create department.

        :param str name: Department name
        :param int parentid: Department parent id
        :param int oder: Order
        :return: Created department's id
        """
        if not name and not parentid:
            raise exceptions.ParamsError(
                "name and parentid can'\t be None"
            )

        body = {
            'name': name,
            'parentid': parentid
        }
        if order:
            body['order'] = order

        data = self.transport.perform_request(
            api='/department/create?access_token=%s' % self.access_token,
            body=body,
            method='POST'
        )
        return data['id']

    @required_params('department_id')
    def update_department(self,
                          department_id=None,
                          name=None,
                          parentid=None,
                          order=None):
        """Update department.

        :param int department_id: Department's id
        :param str name: Department name
        :param int parentid: Department parent id
        :param int oder: Order
        """
        if not department_id:
            raise exceptions.ParamsError('department id is required')
        
        if not name and not parentid and not order:
            return

        body = {
            'id': department_id
        }

        if name:
            body['name'] = name
        
        if parentid:
            body['parentid'] = parentid

        if order:
            body['order'] = order

        self.transport.perform_request(
            api='/department/update?access_token=%s' % self.access_token,
            body=body,
            method='POST'
        )

    @required_params('department_id')
    def delete_department(self, department_id=None):
        """Delete department.

        :param int department_id: Department's id
        """
        if not department_id:
            raise exceptions.ParamsError('department id is required')

        body = {
            'access_token': self.access_token,
            'id': department_id
        }

        self.transport.perform_request(
            api='/department/delete',
            body=body
        )

    @required_params('department_id')
    def list_departments(self, department_id=None):
        """List departments.

        :param int department_id: Department's id
        :return: A list of deparments.
        """
        if not department_id:
            raise exceptions.ParamsError('department id is required')

        body = {
            'access_token': self.access_token,
            'id': department_id
        }

        data = self.transport.perform_request(
            api='/department/list',
            body=body
        )
        return data['department']

    @required_params('name')
    def search_department(self, name=None, fuzzy=0):
        """Search department.

        :param str name: Search keyword
        :param int fuzzy: Fuzzy match or not
        :return: A list of departments.
        """
        if not name:
            return []

        body = {
            'access_token': self.access_token,
            'name': name,
            'fuzzy': fuzzy
        }

        data = self.transport.perform_request(
            api='/department/search',
            body=body
        )
        return data['department']
