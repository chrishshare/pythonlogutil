# coding: utf-8
import os
import sys

from setuptools import setup
from setuptools import find_packages


setup(
    name="pythonlog",
    include_package_data=True,
    version="0.0.1",
    author="chrishshare",
    author_email="chrishshare@163.com",
    description="log tools",
    license="MIT",
    keywords="log logs logutil",
    url="https://github.com/chrishshare/pythonlogutil.git",
    packages=find_packages(),  # include all packages under src
    # package_dir={"": "pythonlog"},
    package_data={"pythonlog": ["config/logger.json"]}
    # data_files=[('./config/logger.json', ['pythonlog/config/logger.json'])]
)
