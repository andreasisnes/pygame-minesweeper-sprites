# -*- coding: utf-8 -*-

from os.path import join, dirname
from setuptools import setup, find_packages
from json import load


def read(fname):
    with open(join(dirname(__file__), fname)) as f:
        return f.read()


def metadata(value):
    with open(join(dirname(__file__), "metadata.json")) as f:
        return load(f)[value]


setup(
    # Package
    name="pygame-minesweeper-sprites",
    version=metadata("version"),
    packages=find_packages(exclude=("tests", "screenshots")),
    url="https://github.com/andreasisnes/Elitekollektivet.Minesweeper.Sprites",
    install_requires=["pygame"],

    zip_safe=False,
    include_package_data=True,

    # Contact
    author="Andreas Isnes Nilsen",
    author_email="andreas.isnes@gmail.com",

    # Description
    description="Minesweeper sprites for pygame applications",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
