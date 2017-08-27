# -*- coding: utf8 -*-
"""
tests.test_helpers.

~~~~~~~~~~~~~~~~~~~

Unittest for helpers.
"""

import pytest

from exmail import helpers
from exmail.exceptions import ParamsError


class TestHelpers(object):

    """Unittest for helpers."""

    def test_required_params(self):
        """Test for required_params decorator."""

        @helpers.required_params()
        def foo1(a=None):
            pass
        foo1()

        @helpers.required_params('a')
        def foo2(a=None):
            pass
        foo2(a=None)

        @helpers.required_params('b')
        def foo3(a=None):
            pass
        with pytest.raises(ParamsError):
            foo3()
