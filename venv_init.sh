#!/usr/bin/env bash

pip install --upgrade pip
pip install -r req.txt
python ask/manage.py makemigrations
python ask/manage.py migrate
gunicorn ask.ask.wsgi -b 0.0.0.0:8000 --pid /tmp/gunicorn1.pid --daemon
gunicorn hello:app -b 0.0.0.0:8080 --pid /tmp/gunicorn2.pid --daemon