#!/bin/sh
# author: deadc0de6 (https://github.com/deadc0de6)
# Copyright (c) 2019, deadc0de6

set -ev

pycodestyle i3altlayout/
pycodestyle setup.py

pyflakes i3altlayout/
pyflakes setup.py

pylint i3altlayout/
pylint i3altlayout/
