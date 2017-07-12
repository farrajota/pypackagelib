#!/usr/bin/env python


import os
from setuptools import setup, find_packages


# Get version
from pypackagelib import VERSION
VERSION = str(VERSION)


# Load requirements
with open('requirements.txt') as f:
    requirements = f.read().splitlines()


setup(
    name='pypackagelib',
    version=VERSION,
    author='M. Farrajota',
    url='https://github.com/farrajota/pypackagelib',
    description='Test package for PyPi + anaconda.',
    long_description="""Test package for PyPi and anaconda integration via travis + appveyor.
        """,
    license='MIT License',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: MacOS X',
        'Environment :: Win32 (MS Windows)',
        'Environment :: X11 Applications',
        'Intended Audience :: Developers',
        'Topic :: Software Development',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    packages=find_packages(exclude=['test']),
    install_requires=requirements
)