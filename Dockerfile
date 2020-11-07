FROM python:3.8-alpine AS build-python
RUN apk update \
    && apk add gcc postgresql-dev musl-dev
COPY ./third_party/ /third_party/
COPY ./requirements.txt /
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /wheels/ -r requirements.txt

FROM python:3.8-alpine
RUN addgroup -S app && adduser -S app -G app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN apk update \
    && apk add postgresql-libs
COPY --from=build-python /wheels/ /wheels/
RUN pip install --no-cache /wheels/*
WORKDIR /code/
COPY --chown=app:app ./budgetsupervisor/ /code/
RUN python manage.py collectstatic --noinput
USER app
CMD gunicorn budgetsupervisor.wsgi:application --bind 0.0.0.0:$PORT
