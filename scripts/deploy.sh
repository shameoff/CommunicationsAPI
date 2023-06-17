#!/bin/bash
export APP_PORT=9996
export APP_CONTAINER_NAME=communications_api_app
export SERVER_NAME=api.shameoff.site
export DEBUG=0
# Настраиваем конфиг nginx.conf
sed -i "s/templateServerName/$SERVER_NAME/g" nginx.conf
sed -i "s/templateAppPort/$APP_PORT/g" nginx.conf
mv nginx.conf /etc/nginx/sites-available/communications_api
ln -s /etc/nginx/sites-available/communications_api /etc/nginx/sites-enabled
service nginx restart

# Запускаем контейнер
if [ "$(docker ps -q -f name=$APP_CONTAINER_NAME)" ]; then
    docker compose down
    docker rm $APP_CONTAINER_NAME
fi
docker compose up -d --build