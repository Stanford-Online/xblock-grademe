"""
XBlock for creating a Grade-Me button
"""
from os import path
from setuptools import setup


version = '1.0.0'
description = __doc__.strip().split('\n')[0]
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.rst')) as file_in:
    long_description = file_in.read()

setup(
    name='xblock-grademe',
    version=version,
    description=description,
    long_description=long_description,
    author='Giulio Gratta',
    author_email='giuliog@stanford.edu',
    url='https://github.com/Stanford-Online/xblock-grademe',
    license='AGPL-3.0',
    packages=[
        'grademebutton',
    ],
    install_requires=[
        'Django<2.0.0',
        'edx-opaque-keys',
        'mock',
        'six',
        'XBlock',
        'xblock-utils',
    ],
    entry_points={
        'xblock.v1': [
            'grademebutton = grademebutton.xblocks:GradeMeButton',
        ],
    },
    package_dir={
        'grademebutton': 'grademebutton',
    },
    package_data={
        'grademebutton': [
            'public/*',
            'scenarios/*.xml',
            'templates/*',
        ],
    },
    classifiers=[
        # https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Operating System :: OS Independent',
        'Programming Language :: JavaScript',
        'Programming Language :: Python',
        'Topic :: Education',
        'Topic :: Internet :: WWW/HTTP',
    ],
    test_suite='grademebutton.tests',
)
