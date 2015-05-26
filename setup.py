from setuptools import setup, find_packages

setup(
    name='interwiki',
    packages=find_packages(),
    version='1.0',
    entry_points={'console_scripts': [
        'interwiki = interwiki.interwiki:main',
    ]}
)
