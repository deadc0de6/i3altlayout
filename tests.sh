#!/usr/bin/env bash
# author: deadc0de6 (https://github.com/deadc0de6)
# Copyright (c) 2019, deadc0de6

set -e

PYTHON_VERSIONS=("3.6" "3.7" "3.8" "3.9" "3.10" "3.11" "3.12" "3.13" "3.14")

test()
{
  python --version

  pycodestyle i3altlayout/
  pycodestyle setup.py

  pyflakes i3altlayout/
  pyflakes setup.py

  pylint \
    --disable=E0012 \
    i3altlayout/
  pylint \
    --disable=E0012 \
    setup.py
}

if [ -n "${GITHUB_WORKFLOW}" ]; then
  # inside runner
  #
  test
else
  if ! hash pyenv &>/dev/null; then
    echo "install pyenv"
    exit 1
  fi

  eval "$(pyenv init -)"
  for PY in "${PYTHON_VERSIONS[@]}"; do
      echo "============== python ${PY} =============="
      pyenv install -s "${PY}"
      pyenv shell "${PY}"
      python -m venv ".venv"
      source ".venv/bin/activate"
      pip install -r requirements.txt
      pip install -r tests-requirements.txt
      test
      deactivate
  done
fi
