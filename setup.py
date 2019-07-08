# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

setup(name='sqlalchemyp',
      version='0.0.1',
      description='SQLAlchemy Print Query',
      author='Evangilo',
      author_email='evangilo@gmail.com',
      packages=find_packages(exclude=('tests', 'docs', 'build')),
      install_requires=['sqlalchemy', 'sqlparse']
      )
