# Python

## Build
```bash
docker build -t python_test .
```

## Run
```bash
docker run -d --rm --name python_test --entrypoint sleep python_test 500
docker exec -it python_test bash
```

## Remove
```bash
docker kill python_test; docker rm python_test; docker image rm python_test
```