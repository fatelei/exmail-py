# -*- coding: utf8 -*-
"""
tests.test_helpers.

~~~~~~~~~~~~~~~~~~~

Unittest for helpers.
"""

<<<<<<< HEAD
import pytest

from exmail import helpers
from exmail.exceptions import ParamsError


class TestHelpers(object):
=======
import unittest
from exmail import helpers


class TestHelpers(unittest.TestCase):
>>>>>>> f1d1af2a982404d6a5886ac69d57796bbafc03d9
    """Unittest for helpers."""

    def test_required_params(self):
        """Test for required_params decorator."""

<<<<<<< HEAD
        @helpers.required_params()
=======
        @helpers.required_params
>>>>>>> f1d1af2a982404d6a5886ac69d57796bbafc03d9
        def foo1(a=None):
            pass
        foo1()

        @helpers.required_params('a')
        def foo2(a=None):
            pass
<<<<<<< HEAD
        foo2(a=None)
=======
        foo2()
>>>>>>> f1d1af2a982404d6a5886ac69d57796bbafc03d9

        @helpers.required_params('b')
        def foo3(a=None):
            pass
<<<<<<< HEAD

        with pytest.raises(ParamsError):
            foo3()
=======
        foo3()
>>>>>>> f1d1af2a982404d6a5886ac69d57796bbafc03d9
