#!/usr/bin/env python

from setuptools import setup

setup(
    name="pyunifi2",
    version="2.22",
    description="API for Ubiquiti Networks UniFi controller",
    author="Tyler Owen",
    author_email="owentl@owentl.com",
    url="https://github.com/owentl/pyunifi2",
    packages=["pyunifi2"],
    scripts=["unifi-create-voucher", "unifi-ls-clients"],
    classifiers=[],
    install_requires=["requests"],
)
