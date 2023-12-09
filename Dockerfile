FROM python:3.12

RUN pip install regex

WORKDIR /app

COPY textFunctions.py /app/textFunctions.py
COPY pattern.txt /app/pattern.txt

CMD ["python3", "textFunctions.py"]