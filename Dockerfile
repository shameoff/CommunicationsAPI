FROM python:3.9-alpine

WORKDIR /app
COPY . .
RUN apk update && pip install -r requirements.txt
RUN python manage.py createsuperuser \
    --no-input \
    --username=admin \
    --email=admin@mail.ru \
    --password=${SUPERUSER_PASSWORD}
# CMD задаётся через docker-compose.yml, чтобы гибко конфигурировать параметры запуска