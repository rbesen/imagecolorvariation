#!/bin/sh
python3 manage.py db upgrade
gunicorn --reload -b :5000 manage:app
