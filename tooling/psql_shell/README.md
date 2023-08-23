# Psql shell status

## Build
```bash
docker build -t psql_shell_status .
```

## Run
```bash
docker run -it --rm \
    -e PGHOST=host_name_or_ip \
    -e PGPORT=5432 \
    -e PGUSER=postgres \
    -e PGPASSWORD=your_password \
    --name psql_shell_status psql_shell_status

docker run -d --rm \
    --entrypoint sleep \
    -e PGHOST=host_name_or_ip \
    -e PGPORT=5432 \
    -e PGUSER=postgres \
    -e PGPASSWORD=your_password \
    --name psql_shell_status psql_shell_status 500

docker exec -it psql_shell_status bash
```

## Remove
```bash
docker kill psql_shell_status; docker rm psql_shell_status; docker image rm psql_shell_status
```