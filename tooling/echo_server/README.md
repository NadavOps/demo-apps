# Echo Server
taken from: `gcr.io/google-containers/echoserver` \
reduced sized and added functionality (port awareness and arm support)

## Build
```bash
docker buildx build \
    -t nadavops/tooling:echo_server \
    --platform "linux/amd64","linux/arm64/v8" \
    --push \
    .
```

## Run
```bash
docker run -d --name echo_server -e PORT="8080" --rm nadavops/tooling:echo_server
docker run -it --name echo_server -e PORT="8080" -p 8080:8080 --rm nadavops/tooling:echo_server
```

## Remove
```bash
docker kill echo_server; docker rm echo_server; docker image rm nadavops/tooling:echo_server
```