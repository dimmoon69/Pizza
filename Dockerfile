FROM python:3.6

ENV PYTHONUNBUFFERED 1

RUN mkdir /pizza

WORKDIR /pizza

ADD . /pizza/

RUN pip install -r requirements.txt
