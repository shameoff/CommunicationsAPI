#!/bin/bash
# VARIABLES: APP_NAME, MY_EMAIL
export APP_CONTAINER_NAME="${APP_NAME}_app"
export DEBUG=0
export APP_PORT=9996
export MINIO_CONSOLE_PORT=9997
export APP_DOMAIN=api.shameoff.site
export MINIO_DOMAIN=minio.shameoff.site

# Дропаем работающий контейнер
if [ "$(docker ps -q -f name="$APP_CONTAINER_NAME")" ]; then
    docker compose down
#    docker rm "$APP_CONTAINER_NAME"
fi
docker compose pull # Подтягиваем новый билд контейнера, если он есть
docker compose up -d --build # Запускаем контейнер
docker exec "$APP_CONTAINER_NAME" python manage.py migrate

# Перемещаем nginx в конфиг nginx сервера и сразу включаем его по правила nginx (мягкая ссылка)
sed -i "s/APP_PORT/$APP_PORT/g" nginx
sed -i "s/APP_DOMAIN/$APP_DOMAIN/g" nginx
sed -i "s/MINIO_PORT/$MINIO_PORT/g" nginx
sed -i "s/MINIO_DOMAIN/$MINIO_DOMAIN/g" nginx

# Перемещаем конфиг и создаём символьную ссылку после перемещения
mv nginx "/etc/nginx/sites-available/${APP_NAME}"
if [ ! -L "/etc/nginx/sites-enabled/$APP_NAME" ]; then
    ln -s "/etc/nginx/sites-available/$APP_NAME" /etc/nginx/sites-enabled
    echo "Symbolic link created."
else
    echo "Symbolic link already exists."
fi

# Проверяем, установлен ли Certbot
if ! command -v certbot &> /dev/null; then
    echo "Certbot не установлен. Установите Certbot для продолжения."
    exit 1
fi

# Проверяем наличие сертификата
certbot certificates -d $APP_DOMAIN -d $MINIO_DOMAIN | grep -q "Expiry Date"
has_certificate=$?

if [ $has_certificate -eq 0 ]; then
    echo "Сертификат существует"
else
    # Сертификат не существует, создаем новый
    echo "Сертификат не существует, создается новый"
    certbot certonly --webroot -w "/var/www/code/$APP_NAME" \
     -d $APP_DOMAIN -d $MINIO_DOMAIN --email "$MY_EMAIL" --agree-tos --no-eff-email
fi

# Проверяем наличие cronjob для автоматического обновления сертификата
if ! crontab -l | grep -q "certbot renew"; then
    # cronjob нет, создаем новую
    echo "0 0 1 * * certbot renew" | crontab -
    echo "Создана cronjob для автоматического обновления сертификата."
else
    echo "cronjob для автоматического обновления уже существует."
fi
