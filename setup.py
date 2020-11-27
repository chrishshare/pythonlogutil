# coding: utf-8
import os
import sys

from setuptools import setup
from setuptools import find_packages


__author__ = 'chrishshare <chrishshare@163.com>'


with open('README.md') as readme_file:
    long_description = readme_file.read()


# 'setup.py publish' shortcut.
if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist bdist_wheel')
    os.system('twine upload dist/*')
    sys.exit()
elif sys.argv[-1] == 'clean':
    import shutil
    if os.path.isdir('build'):
        shutil.rmtree('build')
    if os.path.isdir('dist'):
        shutil.rmtree('dist')
    if os.path.isdir('chromedriver_autoinstaller.egg-info'):
        shutil.rmtree('chromedriver_autoinstaller.egg-info')


setup(
    name="pythonlog",
    version="0.0.1",
    author="chrishshare",
    author_email="chrishshare@163.com",
    description="log tools",
    license="MIT",
    keywords="log logs logutil",
    url="https://github.com/yeongbin-jo/python-chromedriver-autoinstaller",
    packages=find_packages(where='pythonlog', include=['*']),
    package_dir={"": "pythonlog"},
    data_files=[('./config/logger.json', ['pythonlog/config/logger.json'])]
)
