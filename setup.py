# -*- coding: utf8 -*-

from setuptools import setup, find_packages

from exmail import __version__


setup(
    name='exmail',
    description='exmail python client lib',
    version=__version__,
    author='fatelei',
    author_email='fatelei@gmail.com',
    packages=find_packages(
        where='.',
        exclude=('tests',)
    ),
    install_requires=[],
    test_requires=[],
)
