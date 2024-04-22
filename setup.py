from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='CMPSC441PIFI',
    version='0.1',
    # Exclude my own project as it's not meant to be a package
    packages=find_packages(exclude=['CMPSC441PIFI']),
    install_requires=requirements,
)