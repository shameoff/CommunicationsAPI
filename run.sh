#!/bin/sh

python manage.py makemigrations
python manage.py migrate --no-input

python manage.py runserver 8080


