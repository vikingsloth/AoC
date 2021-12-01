#!/usr/bin/env python

from setuptools import find_packages, setup

setup(
    name = 'aoc',
    version = '20.21',
    description = 'advent of code library',
    author = 'vikingsloth',
    author_email = 'vikingsloth@htols.net',
    url = 'https://github.com/vikingsloth',
    packages = find_packages(),
    scripts = ['aoccli']
)
