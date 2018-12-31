#!/usr/bin/env python

from distutils.core import setup

setup(name='pyAI',
      version='0.1dev',
      description='Python AI for games',
      author='Joe Yuan',
      author_email=''.join(chr(i) for i in [106, 111, 101, 46, 121, 117, 97, 110, 49, 57, 64, 103, 109, 97, 105, 108, 46, 99, 111, 109]),
      packages=['pyAI'],
      long_description=open('README.txt').read(),
)
