FROM python:3

RUN pip install regex

WORKDIR /app

COPY textFunctions.py /app/textFunctions.py

