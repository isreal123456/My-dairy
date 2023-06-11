#!/usr/bin/env bash

set -o errexit  # exit on errexit

pip install -r requirements.txt

python manage.py collectstatic --no-install
python manage.py migrate