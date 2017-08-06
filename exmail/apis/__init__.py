# -*- coding: utf8 -*-
"""
exmail.apis.

~~~~~~~~~~~~

Apis.
"""

from .department import DepartmentApi
from .group import GroupApi
from .sso import SSOApi
from .user import UserApi

__all__ = [
    'DepartmentApi',
    'GroupApi',
    'SSOApi',
    'UserApi'
]
