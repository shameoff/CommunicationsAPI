#!/bin/bash

# Перемещаем nginx.conf в конфиг nginx сервера и сразу включаем его по правила nginx (мягкая ссылка)
sed -i "s/templateServerName/$APP_DOMAIN/g" nginx.conf
sed -i "s/templateAppPort/$APP_PORT/g" nginx.conf
mv nginx.conf "/etc/nginx/sites-available/${APP_NAME}"
ln -s "/etc/nginx/sites-available/${APP_NAME}" /etc/nginx/sites-enabled

# Проверяем, установлен ли Certbot
echo "Time before checking if installed $(date +%T)"
if ! command -v certbot &> /dev/null; then
    echo "Certbot не установлен. Установите Certbot для продолжения."
    exit 1
fi
echo "Time after checking if installed $(date +%T)"

# Проверяем наличие сертификата
certbot certificates --domains "$APP_DOMAIN" | grep -q "Expiry Date"
has_certificate=$?

echo "Time before checking if cert exists $(date +%T)"
if [ $has_certificate -eq 0 ]; then
    # Сертификат уже существует, проверяем, нужно ли его обновить
    certbot renew --dry-run
else
    # Сертификат не существует, создаем новый
    certbot certonly --webroot -w "/var/www/code/$APP_NAME" -d "$APP_DOMAIN" --email "$MY_EMAIL" --agree-tos
fi
echo "Time after checking if cert exists $(date +%T)"

# Часть конфигурации, которая вставляется в конфиг сервера, чтобы автоматически конфигурировать сертификат
CERT_CONFIG="listen 443 ssl; # managed by Certbot
  ssl_certificate /etc/letsencrypt/live/$APP_DOMAIN/fullchain.pem; # managed by Certbot
  ssl_certificate_key /etc/letsencrypt/live/$APP_DOMAIN/privkey.pem; # managed by Certbot
  include /etc/letsencrypt/options-ssl-nginx.conf; # managed by Certbot
  ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem; # managed by Certbot
} server {
    if (\$host = $APP_DOMAIN) {
        return 301 https://\$host\$request_uri;
    } # managed by Certbot

    listen 80;
    server_name $APP_DOMAIN;
    return 404; # managed by Certbot"

awk -v cert_config="$CERT_CONFIG" -v app_name="$APP_NAME" '
BEGIN {
  RS = ""
  ORS = "\n\n"
}
{
  gsub("# INSERT_CERT_CONFIG_HERE", cert_config)
  print
}
' "/etc/nginx/sites-available/$APP_NAME" > temp_file && mv temp_file "/etc/nginx/sites-available/$APP_NAME"
echo "Time after awk replacing $(date +%T)"

# Проверяем наличие cronjob для автоматического обновления
if ! crontab -l | grep -q "certbot renew"; then
    # cronjob нет, создаем новую
    echo "0 0 1 * * certbot renew" | crontab -
    echo "Создана cronjob для автоматического обновления сертификата."
else
    echo "cronjob для автоматического обновления уже существует."
fi
echo "Time after crontab creating $(date +%T)"
