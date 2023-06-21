FROM python:3.9-alpine

WORKDIR /app
COPY . .
RUN apk update && pip install -r requirements.txt

# CMD задаётся через docker-compose.yml, чтобы гибко конфигурировать параметры запуска