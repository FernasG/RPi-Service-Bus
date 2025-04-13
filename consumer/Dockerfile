ARG PYTHON_VERSION=3.12.3
ARG PIP_VERSION=25.0.1

FROM docker.io/python:${PYTHON_VERSION}-slim

ARG PIP_VERSION
ENV PIP_VERSION ${PIP_VERSION}

RUN python3 -m pip install --upgrade pip==${PIP_VERSION}

WORKDIR /app

COPY requirements.txt /app

RUN pip3 install -r requirements.txt

COPY . .

CMD ["tail", "-f", "/dev/null"]