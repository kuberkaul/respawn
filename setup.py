#!/usr/bin/env python

""" Setup script. Used by easy_install and pip. """

import os
from setuptools import setup, find_packages
from setuptools.command.test import test
import sys


class Tox(test):
    user_options = [('tox-args=', 'a', "Arguments to pass to tox")]

    def initialize_options(self):
        test.initialize_options(self)
        self.tox_args = None

    def finalize_options(self):
        test.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import tox
        import shlex
        args = self.tox_args
        if args:
            args = shlex.split(self.tox_args)
        errno = tox.cmdline(args=args)
        sys.exit(errno)


def get_version():
    try:
        # get version from './VERSION'
        src_root = os.path.dirname(__file__)
        if not src_root:
            src_root = '.'

        with open(src_root + '/VERSION', 'r') as f:
            version = f.readline ().strip()

        return version

    except Exception, e:
        raise RuntimeError('Could not extract version: %s' % e)

setup_args = {
    'name': 'respawn',
    'version': get_version(),
    'description': 'AWS CloudFormation Template generator from Yaml specifications.',
    'url': 'http://radical-cybertools.github.io/saga-python/',
    'license': 'ISC',
    'keywords': 'aws cloudformation yaml',
    'classifiers': [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Environment :: Console',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5'
        'Topic :: Utilities',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX',
        'Operating System :: Unix'
    ],
    'packages': find_packages(),
    'package_data': {'respawn': ['VERSION']},
    'entry_points': {
        'console_scripts': [
            'respawn=respawn.cli:generate',
        ],
    },
    'install_requires': [
        'cfn-pyplates',
        'Jinja2'
    ],
    'tests_require': ['tox'],
    'cmdclass': {'test': Tox},
    'zip_safe': False,
}

setup(**setup_args)
