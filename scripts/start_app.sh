#!/bin/bash
export APP_NAME=$APP_NAME
export APP_CONTAINER_NAME="${APP_NAME}_app"
export DEBUG=0

# Запускаем контейнер
if [ "$(docker ps -q -f name="$APP_CONTAINER_NAME")" ]; then
    docker compose down
    docker rm "$APP_CONTAINER_NAME"
fi
docker compose up -d --build
docker exec "$APP_CONTAINER_NAME" python manage.py migrate