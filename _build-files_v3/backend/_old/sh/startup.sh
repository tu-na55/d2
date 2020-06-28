#!/bin/sh

APP_DIR=/var/www/app/sample

${APP_DIR}/manage.py migrate
${APP_DIR}/manage.py loaddata user.yaml

uwsgi --ini /etc/uwsgi/vassals/api.ini
