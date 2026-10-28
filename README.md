# functions-from-zero

[![Python application test with Github Actions](https://github.com/ufuos10/functions-from-zero/actions/workflows/main.yml/badge.svg)](https://github.com/ufuos10/functions-from-zero/actions/workflows/main.yml)


### To call Microservice

```bash
curl -X 'POST' \
  'http://127.0.0.1:8080/wiki' \
  -H 'accept: */*' \
  -H 'Content-Type: application/json' \
  -d '{
  "title": "Lebron James"
}'
```

```
Change to codespace url once codespace becomes active again
```

### Build container
`docker build .`
`docker image ls --all`

### Run container
`docker run -p 127.0.0.1:8080:8080 image_id_here`

### Invoke POST request

run `bash invoke.sh`