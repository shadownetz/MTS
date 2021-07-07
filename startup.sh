#!/bin/sh
#source venv/bin/activate
gunicorn --bind :8000 --workers 3 MTS.wsgi:application