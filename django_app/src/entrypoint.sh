#!/bin/bash
#python manage.py collectstatic --noinput &&
python manage.py makemigrations &&
python manage.py migrate &&
python manage.py create_kafka_topic
python manage.py create_es_index
# gunicorn --config gunicorn_conf.py config.wsgi:application
python ./manage.py runserver 0.0.0.0:8000
