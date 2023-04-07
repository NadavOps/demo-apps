FROM python:3.9.16-alpine3.17
# FROM python:3.9-slim-buster

ENV PORT=8080

WORKDIR /app

# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

CMD [ "python", "app.py" ]
