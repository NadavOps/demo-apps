# NginX dynamic_env_message_page

## Build
```bash
docker buildx build \
    -t nadavops/nginx:dynamic_env_message_page \
    --platform "linux/amd64","linux/arm64/v8" \
    --push \
    .
```

## Run
```bash
docker run -d --name dynamic_env_message_page -p 8080:80 \
    -e MESSAGE="Hello, world" \
    -e BACKGROUND_COLOR="white" \
    nadavops/nginx:dynamic_env_message_page
```

## Remove
```bash
docker kill dynamic_env_message_page; docker rm dynamic_env_message_page; docker image rm nadavops/nginx:dynamic_env_message_page
```