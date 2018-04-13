from setuptools import setup

requires = [
    'pyramid',
    'waitress',
    'python-dateutil'
]

setup(name='hello',
      install_requires=requires,
      package_dir={'': "hello"},
      entry_points="""\
      [paste.app_factory]
      main = hello:main
      """,
      )
