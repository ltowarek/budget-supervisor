FROM python:3.8

RUN groupadd -g 1000 app
RUN useradd -u 1000 -g app -s /bin/sh -m app
USER app

ENV PATH="/home/app/.local/bin/:${PATH}"
