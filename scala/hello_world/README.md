# Scala hello world

## build
```bash
docker buildx build \
    -t nadavops/scala:hello_world \
    --platform "linux/amd64" \
    --push \
    .
```

## run
```bash
docker run --name scala_hello_world nadavops/scala:hello_world
```

## remove
```bash
docker kill scala_hello_world; docker rm scala_hello_world; docker image rm nadavops/scala:hello_world
```