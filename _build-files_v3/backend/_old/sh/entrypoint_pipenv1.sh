#!/bin/sh

if [[ -z "${VIRTUAL_ENV}" ]]; then
    source "$(pipenv --venv)/bin/activate"
fi

exec "$@"
