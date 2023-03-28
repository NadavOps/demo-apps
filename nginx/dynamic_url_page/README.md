# NginX dynamic_url_page

## build
```bash
docker buildx build \
    -t nadavops/nginx:dynamic_url_page \
    --platform "linux/amd64","linux/arm64/v8" \
    --push \
    .
```

## run
```bash
docker run -d --name dynamic_url_page -p 8080:80 nadavops/nginx:dynamic_url_page
```

## remove
```bash
docker kill dynamic_url_page; docker rm dynamic_url_page; docker image rm nadavops/nginx:dynamic_url_page
```