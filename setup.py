# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='war_card_game',
    version='1.0.0',
    description='Sample package for Python-Guide.org',
    long_description=readme,
    author='Antonio Martín',
    author_email='amartinescalera@gmail.com',
    url='https://github.com/amartinescalera/WarCardName',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

