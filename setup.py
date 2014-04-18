from setuptools import setup, find_packages
import sys, os

version = '0.0'

setup(name='lfs_trackactivity',
      version=version,
      description="Django LFS ecommerce activity tracker",
      long_description="""\
Activity tracker powered by adform.com""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='Python Django ecommerce',
      author='Davide Moro',
      author_email='davide.moro@redomino.com',
      url='http://redomino.com',
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
