from setuptools import setup, find_packages
import os

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

version = '0.1dev'

long_description = (
      read('README.txt')
      + '\n' +
      'Change history\n'
      '**************\n'
      + '\n' +
      read('CHANGES.txt')
      )

setup(name='lfs_trackactivity',
      version=version,
      description="Django LFS ecommerce activity tracker",
      long_description=long_description,
      classifiers=["Framework :: Django",
                   "Programming Language :: Python",], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='Python Django ecommerce',
      author='Davide Moro',
      author_email='davide.moro@redomino.com',
      url='https://github.com/redomino/lfs_trackactivity',
      license='GPL',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
