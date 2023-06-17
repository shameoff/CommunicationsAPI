#!/bin/bash
export APP_PORT=9996
export APP_CONTAINER_NAME="${APP_NAME}_app"
export DEBUG=0

echo "Проверка переменных окружения внутри deploy.sh. SERVER_NAME = $SERVER_NAME;
APP_NAME = $APP_NAME; MY_EMAIL = $MY_EMAIL"

# Настраиваем конфиг nginx.conf
sed -i "s/templateServerName/$SERVER_NAME/g" nginx.conf
sed -i "s/templateAppPort/$APP_PORT/g" nginx.conf
mv nginx.conf "/etc/nginx/sites-available/${APP_NAME}"
ln -s "/etc/nginx/sites-available/${APP_NAME}" /etc/nginx/sites-enabled
service nginx restart

# Запускаем контейнер
if [ "$(docker ps -q -f name="$APP_CONTAINER_NAME")" ]; then
    docker compose down
    docker rm "$APP_CONTAINER_NAME"
fi
docker compose up -d --build
docker exec "$APP_CONTAINER_NAME" python manage.py migrate