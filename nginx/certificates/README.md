# NginX certificates_nginx
# Still needs to make this more dynamic, not sure if $SERVER works correctly

## Build
```bash
docker build -t certificates_nginx .

docker buildx build \
    -t nadavops/nginx:certificates_nginx \
    --platform "linux/amd64","linux/arm64/v8" \
    --push \
    .
```

## Run
```bash
docker run -d -p 443:443 \
    -v /path/to/ssl/certificate:/etc/nginx/ssl/certificate.pem \
    -v /path/to/ssl/key:/etc/nginx/ssl/key.pem \
    -e SERVER_NAME=change_here.com \
    --name certificates_nginx certificates_nginx
```

## Remove
```bash
docker kill certificates_nginx; docker rm certificates_nginx; docker image rm nadavops/nginx:certificates_nginx
```