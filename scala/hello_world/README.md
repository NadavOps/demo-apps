# Scala hello world

## Build
```bash
docker buildx build \
    -t nadavops/scala:hello_world \
    --platform "linux/amd64" \
    --push \
    .
```

## Run
```bash
docker run --name scala_hello_world nadavops/scala:hello_world
```

## Remove
```bash
docker kill scala_hello_world; docker rm scala_hello_world; docker image rm nadavops/scala:hello_world
```