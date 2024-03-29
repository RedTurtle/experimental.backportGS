from setuptools import setup, find_packages
import os

version = '0.2.2.dev0'

setup(name='experimental.backportGS',
      version=version,
      description="Monkey-patch Plone 3 to make Plone 4 Generic Setup import steps to continue working",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Framework :: Plone :: 3.3",
        "Development Status :: 4 - Beta",
        "Programming Language :: Python",
        ],
      keywords='plone generic-setup backport',
      author='RedTurtle Technology',
      author_email='sviluppoplone@redturtle.it',
      url='https://github.com/RedTurtle/experimental.backportGS',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['experimental'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'Products.CMFPlone<=4.0b1',
          'collective.monkeypatcher>1.0',
      ],
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
