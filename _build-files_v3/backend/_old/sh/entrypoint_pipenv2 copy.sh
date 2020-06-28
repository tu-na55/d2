#!/bin/sh

pipenv --venv > /dev/null || pipenv install --skip-lock --dev --ignore-pipfile
