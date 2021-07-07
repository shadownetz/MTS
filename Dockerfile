# Python and Linux version
FROM python:3.8-alpine
COPY requirements.txt /app/requirements.txt

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG 0

# install psycopg2
#RUN apt update \
#    && apt add --virtual build-deps gcc python3-dev musl-dev \
#    && apt add postgresql-dev \
#    && pip install psycopg2 \
#    && apt del build-deps

# Configure server
RUN set -ex \
#    && python3 -m venv /app/venv \
#    && source /app/venv/bin/activate \
    && pip3 install --upgrade pip \
    && pip3 install -r /app/requirements.txt

RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add postgresql \
    && apk add postgresql-dev \
    && pip3 install psycopg2 \
    && apk add jpeg-dev zlib-dev libjpeg \
    && pip3 install Pillow \
    && pip install django-heroku \
    && apk del build-deps

# copy project
ADD . .

# add and run as non-root user
#RUN adduser -D myuser
#USER myuser

#EXPOSE 8000

# run gunicorn
#CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "MTS.wsgi:application"]
#CMD gunicorn --bind :8000 --workers 3 MTS.wsgi:application
CMD gunicorn MTS.wsgi:application --bind 0.0.0.0:$PORT


