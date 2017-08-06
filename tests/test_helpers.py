# -*- coding: utf8 -*-
"""
tests.test_helpers.

~~~~~~~~~~~~~~~~~~~

Unittest for helpers.
"""

import unittest
from exmail import helpers


class TestHelpers(unittest.TestCase):
    """Unittest for helpers."""

    def test_required_params(self):
        """Test for required_params decorator."""

        @helpers.required_params
        def foo1(a=None):
            pass
        foo1()

        @helpers.required_params('a')
        def foo2(a=None):
            pass
        foo2()

        @helpers.required_params('b')
        def foo3(a=None):
            pass
        foo3()
