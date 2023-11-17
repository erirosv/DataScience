from setuptools import setup, find_packages

#setup(name='datascience', version='0.1', packages=find_packages())

#!/usr/bin/env python3

from pathlib import Path
from setuptools import setup

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
    #packages=['data_helpers', 'utils'],
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ],
    include_package_data=True
)