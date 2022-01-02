from os import path

from setuptools import setup

this_directory = path.abspath(path.dirname(__file__))
readme_path = path.join(this_directory, 'README.md')

with open(readme_path, encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name='snowflake',
    version='0.1',
    packages=['Snowflake'],
    url='https://github.com/ronmorgen1/snowflake',
    license='MIT',
    author='Ron Morgenstern',
    author_email='ron.morgenstern@pagaya.com',
    description='Simple python wrapper for the Snowflake API',
    install_requires=['pandas', 'sqlalchemy', 'snowflake-connector-python'],
)
