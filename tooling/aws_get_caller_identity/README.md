# Sleep

## Build
```bash
docker buildx build \
    -t nadavops/tooling:aws_get_caller_identity \
    --platform "linux/amd64","linux/arm64/v8" \
    --push \
    .
```

## Run
```bash
docker run -it --rm --name aws_get_caller_identity nadavops/tooling:aws_get_caller_identity
```

## Remove
```bash
docker kill aws_get_caller_identity; docker rm aws_get_caller_identity; docker image rm nadavops/tooling:aws_get_caller_identity
```