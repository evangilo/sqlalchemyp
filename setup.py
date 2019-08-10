# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

with open('README.md') as f:
    readme = f.read()

setup(name='sqlalchemyp',
      version='0.0.4',
      description='SQLAlchemy Print Query',
      long_description=readme,
      long_description_content_type='text/markdown',
      author='Evangilo',
      author_email='evangilo@gmail.com',
      packages=find_packages(exclude=('tests', 'docs', 'build')),
      install_requires=['sqlalchemy', 'sqlparse'],
      license=u'MIT',
      classifiers=[
          'Intended Audience :: Developers',
          'Programming Language :: Python',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
      ])
