# -*- coding: utf8 -*-

import functools


def required_params(*required):
    """Check required params."""
    def wrapper(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            keys = set(kwargs.keys())
            if not (set(required) - keys):
                return func(*args, **kwargs)
            else:
                raise Exception('required params are {}, but params passed are {}'.format(
                    required, kwargs
                ))
        return inner
    return wrapper
