#!/usr/bin/env python3

from pathlib import Path
from setuptools import setup, find_packages

directory = Path(__file__).resolve().parent
with open(directory / 'README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='myproject',
    version='1.0.0',
    description='A short description of my project',
    author='Your Name',
    license='MIT',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    include_package_data=True
)