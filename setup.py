#!/usr/bin/env python


"""
Setup script for gpsdio-bigquery-schema
"""


import os
from setuptools import setup


with open('README.rst') as f:
    readme = f.read().strip()


with open('LICENSE.txt') as f:
    license = f.read().strip()


version = None
author = None
email = None
source = None
with open(os.path.join('gpsdio_bigquery_schema', '__init__.py')) as f:
    for line in f:
        if line.strip().startswith('__version__'):
            version = line.split('=')[1].strip().replace('"', '').replace("'", '')
        elif line.strip().startswith('__author__'):
            author = line.split('=')[1].strip().replace('"', '').replace("'", '')
        elif line.strip().startswith('__email__'):
            email = line.split('=')[1].strip().replace('"', '').replace("'", '')
        elif line.strip().startswith('__source__'):
            source = line.split('=')[1].strip().replace('"', '').replace("'", '')
        elif None not in (version, author, email, source):
            break


setup_args = dict(
    author=author,
    author_email=email,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Communications',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: GIS',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Utilities',
    ],
    description="A CLI plugin for `gpsdio` that produces a schema file for BigQuery to be used together with CSV output from gpsdio-csv for exporting data into Google's BigQuery.",
    entry_points='''
        [gpsdio.gpsdio_plugins]
        bigquery_schema=gpsdio_bigquery_schema.core:gpsdio_bigquery_schema
    ''',
    extras_require={
        'test': ['pytest', 'pytest-cov']
    },
    include_package_data=True,
    install_requires=[
        'click>=3.0',
        'gpsdio>=0.0.2',
        'msgpack-python>=0.4.6'
    ],
    keywords='AIS GIS remote sensing BigQuery',
    license=license,
    long_description=readme,
    name='gpsdio-bigquery-schema',
    packages=['gpsdio_bigquery_schema'],
    url=source,
    version=version,
    zip_safe=True
)


setup(**setup_args)
