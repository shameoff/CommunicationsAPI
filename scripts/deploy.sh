#!/bin/bash
export APP_PORT=9996
export SERVER_NAME=api.shameoff.site

# Настраиваем конфиг nginx.conf
sed -i "s/\templateServerName/$SERVER_NAME/g" nginx.conf
sed -i "s/\templateAppPort/$APP_PORT/g" nginx.conf
mv nginx.conf /etc/nginx/sites-available/communications_api
ln -s /etc/nginx/sites-available/communications_api /etc/nginx/sites-enabled
service nginx restart

# Запускаем контейнер
docker compose up -d