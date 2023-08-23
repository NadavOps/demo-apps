# Psql status

## Build
```bash
docker build -t psql_status .
```

## Run
```bash
docker run -it --rm \
    -e HOST=host_name_or_ip \
    -e PORT=5432 \
    -e USER=postgres \
    -e PASS=your_password \
    --name psql_status psql_status
docker exec -it psql_status bash
```

## Remove
```bash
docker kill psql_status; docker rm psql_status; docker image rm psql_status
```