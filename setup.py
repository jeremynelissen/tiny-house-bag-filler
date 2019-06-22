#!/usr/bin/env python
from setuptools import find_packages, setup

VERSION = '0.1.0.dev0'

setup(
    name='tiny-house-bag-filler',
    version=VERSION,
    description='Raspberry Pi package for filling cold brew coffee bags',
    packages=find_packages(exclude=['tests*']),
    install_requires=[
        'gpiozero==1.5.0'
    ],
    include_package_data=True,
    test_suite='tests',
    maintainer='Jeremy Nelissen',
    maintainer_email='jeremynelissen@users.noreply.github.com',
    url='https://github.com/jeremynelissen/tiny-house-bag-filler'
)