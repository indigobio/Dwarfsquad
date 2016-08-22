from distutils.core import setup

import ez_setup
ez_setup.use_setuptools()

from setuptools import find_packages


setup(name='dwarfsquad',
      version='2.1.0',
      description='Assay Configuration Interchange tool.',
      author='Kenneth Tussey',
      author_email='whereskenneth@gmail.com',
      scripts=['dwarfsquad/dwarfsquad'],
      packages=find_packages())
