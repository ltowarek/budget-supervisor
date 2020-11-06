FROM python:3.8-alpine

WORKDIR /code/

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add gcc postgresql-dev musl-dev

COPY ./third_party/ /code/third_party/
COPY ./requirements.txt /code/
RUN pip install -r requirements.txt

COPY ./budgetsupervisor/ /code/

RUN python manage.py collectstatic --noinput

RUN adduser -D djangouser
USER djangouser

CMD gunicorn budgetsupervisor.wsgi:application --bind 0.0.0.0:$PORT
