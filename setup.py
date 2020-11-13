# -*- coding: utf-8 -*-

# from distutils.core import setup

from setuptools import setup, find_packages

try:
    long_description = open("README.rst").read()
except IOError:
    long_description = ""

setup(
    name="pandas-preprocessor",
    version="0.1.0",
    description="A package for preprocessing and encoding columns",
    license="MIT",
    author="manyu",
    packages=find_packages(
        include=['pandas-preprocessor', 'pandas-preprocessor.*']),
    install_requires=[
        "tpot",
        "sklearn"
    ],
    long_description=long_description,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
    ]
)
