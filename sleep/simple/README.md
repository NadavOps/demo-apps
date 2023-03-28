# Sleep simple

## build
```bash
docker buildx build \
    -t nadavops/sleep:simple \
    --platform "linux/amd64","linux/arm64/v8" \
    --push \
    .
```

## run
```bash
docker run -d --name sleep_simple -e SLEEP_TIME="5" nadavops/sleep:simple
```

## remove
```bash
docker kill sleep_simple; docker rm sleep_simple; docker image rm nadavops/sleep:simple
```