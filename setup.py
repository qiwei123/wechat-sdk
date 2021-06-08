#!/usr/bin/env python
from io import open

from setuptools import setup, find_packages


with open('requirements.txt') as f:
    requirements = [l for l in f.read().splitlines() if l]

setup(name="wechat-sdk",
      version="1.1.1",
      install_requires=requirements,
      packages=find_packages(),
      url='https://git.corp.qianka.com/qi.wei/wechat-sdk')
