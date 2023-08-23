FROM python:3.11.4-slim

COPY ./requirements.txt /
RUN pip install --upgrade pip && pip install --no-cache-dir -r /requirements.txt

WORKDIR /app
COPY . /app

ENTRYPOINT [ "python3" ]

CMD ["psql_status.py"]
