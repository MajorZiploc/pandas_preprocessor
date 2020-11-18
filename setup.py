# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

try:
    long_description = open("README.rst").read()
except IOError:
    long_description = "Please visit the github page for documentation. https://github.com/MajorZiploc/pandas_preprocessor"

setup(
    name="pandas_preprocessor",
    version="0.2.3",
    description="A package for preprocessing and encoding columns",
    license="MIT",
    author="Manyu Lakhotia",
    packages=find_packages(
        include=['pandas_preprocessor', 'pandas_preprocessor.*', 'dist']),
    long_description=long_description,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
    ],
    install_requires=[
        'numpy',
        'scikit-learn',
        'pandas',
        'toml',
        'joblib'
    ]
)
