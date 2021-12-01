# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open("README.rst") as f:
    readme = f.read()

with open("LICENSE") as f:
    license_ = f.read()

setup(
    name="AdventOfCode2021",
    version="0.1.0",
    description="Advent of Code 2021 solutions",
    long_description=readme,
    author="Patrick Kodal",
    author_email="patrick@kodal.dev",
    url="https://github.com/ladokp/AdventOfCode2021",
    license=license_,
    packages=find_packages(exclude=("tests", "docs")),
)
