FROM python:3.12

WORKDIR /app

COPY server.py /app/server.py
COPY output.py /app/output.py
COPY textSegmentation.py /app/textSegmentation.py
COPY dockerController.py /app/dockerController.py

CMD ["python3", "server.py"]