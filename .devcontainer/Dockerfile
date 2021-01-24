FROM python:3.8

RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends curl firefox-esr

RUN curl -L https://github.com/mozilla/geckodriver/releases/download/v0.29.0/geckodriver-v0.29.0-linux64.tar.gz | \
    tar xz -C /usr/local/bin/ && \
    chmod +x /usr/local/bin/geckodriver

RUN groupadd -g 1000 app
RUN useradd -u 1000 -g app -s /bin/sh -m app
USER app

ENV PATH="/home/app/.local/bin/:${PATH}"

CMD ["/bin/bash"]
