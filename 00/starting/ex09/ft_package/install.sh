#!/bin/bash

python setup.py sdist bdist_wheel

# pip install dist/ft_package-0.0.1.tar.gz
pip install dist/ft_package-0.0.1-py3-none-any.whl
