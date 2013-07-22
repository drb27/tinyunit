#!/usr/bin/env python3

from setuptools import setup,find_packages
import tinyunit

setup(
    name='tinyunit',
    version = tinyunit.__version__,
    description='Minimal unit test framework',
    author='David Bradshaw',
    author_email='david.bradshaw.usa@gmail.com',
    packages=find_packages(),
    install_requires=['setuptools']
)

