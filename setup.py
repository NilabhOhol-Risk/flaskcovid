#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import subprocess
import pip
import sys


REQUIREMENTS = [
    'Pygments',
    'appnope',
    'awscli',
    'boto3',
    'cachetools',
    'docutils',
    'et-xmlfile',
    'google-api-python-client',
    'google-auth',
    'jdcal',
    'jedi',
    'knotr',
    'networkx',
    'numpy',
    'oauth2client',
    'openpyxl',
    'pandas',
    'parso',
    'psycopg2',
    'pytest',
    'python-oauth2',
    'pytz',
    'pyyaml',
    'requests',
    'rsa',
    'scikit-learn',
    'scipy',
    'slacker',
    'sqlacodegen',
    'sqlalchemy',
    'sqlparse',
    'statsmodels',
    'toolz',
    'tqdm',
    'urllib3',
    'uszipcode',
    'xlrd',
    'xmltodict',
    'PureCloudPlatformClientV2'
]


setup(
    name='flaskcovid',
    version='0.1.0',
    description="Flask Setup for COSMOS COVID-19 LP Project",
    author="Nilabh Ohol",
    author_email='nilabh30@gmail.com',
    #url='',
    packages=find_packages(),
    package_dir={'flaskcovid':'flaskcovid'},
    include_package_data=True,
    install_requires=REQUIREMENTS,
    zip_safe=False,
    keywords='Flask Setup for COSMOS COVID-19 LP Project',
    classifiers=[
        'Programming Language :: Python :: 3.7',
    ]
)
