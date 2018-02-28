# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='tamagochi',
    version='0.0.1',
    description='Package for testing',
    long_description=readme,
    author='Antonio Linde',
    author_email='antonio.linde',
    url='https://github.com/alinde1/tamagochi',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)