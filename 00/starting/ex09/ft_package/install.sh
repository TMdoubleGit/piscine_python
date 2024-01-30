#!/bin/bash

# Générer les fichiers de distribution
python setup.py sdist bdist_wheel

# Installer le package localement
pip install dist/ft_package-0.0.1.tar.gz
# ou
# pip install dist/ft_package-0.0.1-py3-none-any.whl
