# Sleep

## build
```bash
docker buildx build \
    -t nadavops/tooling:sleep \
    --platform "linux/amd64","linux/arm64/v8" \
    --push \
    .
```

## run
```bash
docker run -d --name sleep -e SLEEP_TIME="5" --rm nadavops/tooling:sleep
```

## remove
```bash
docker kill sleep; docker rm sleep; docker image rm nadavops/tooling:sleep
```