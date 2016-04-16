from distutils.core import setup

import ez_setup
ez_setup.use_setuptools()

from setuptools import find_packages


setup(name='dwarfsquad',
      version='2.0.0rc2',
      description='Assay Configuration Interchange tool.',
      author='Kenneth Tussey',
      author_email='whereskenneth@gmail.com',
      scripts = ['dwarfsquad/dwarfsquad'],
      packages= find_packages(),
      install_requires=['pymongo', 'behave>=1.2', 'requests==2.1.0', 'pyaml', 'tqdm>=1.0', 'requests_cache>=0.4.4'])