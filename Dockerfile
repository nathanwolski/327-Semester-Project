FROM python:3.12

WORKDIR /app

RUN pip install flask

COPY textFunctions.py /app/textFunctions.py

