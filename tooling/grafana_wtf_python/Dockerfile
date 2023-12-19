FROM python:3.11.4-slim

COPY ./requirements.txt /
RUN pip install --upgrade pip && pip install --no-cache-dir -r /requirements.txt

WORKDIR /app
COPY . /app

ENV GRAFANA_URL="https://grafana.org/"
ENV GRAFANA_TOKEN=""

ENTRYPOINT [ "python3" ]

CMD ["grafana_wtf.py"]
