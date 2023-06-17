#!/bin/bash

# Переменные. Также сюда APP_NAME из env
DOMAIN="$SERVER_NAME"
EMAIL="$MY_EMAIL"
CRONJOB_NAME="certbot-renew"

# Проверяем, установлен ли Certbot
if ! command -v certbot &> /dev/null; then
    echo "Certbot не установлен. Установите Certbot для продолжения."
    exit 1
fi

# Проверяем наличие сертификата
certbot certificates --domains "$DOMAIN" | grep -q "Expiry Date"
has_certificate=$?

if [ $has_certificate -eq 0 ]; then
    # Сертификат уже существует, проверяем, нужно ли его обновить
    certbot renew --dry-run
    echo "Дебаг. Сертификат проверили"
else
    echo "Дебаг. Сертификат создаётся новый"
    # Сертификат не существует, создаем новый
    certbot certonly --webroot -w "/var/www/code/$APP_NAME" -d "$DOMAIN" --email "$EMAIL" --agree-tos
fi

echo "Дебаг.Дошли до переменной CERT_CONFIG"

# Часть конфигурации, которая вставляется в конфиг сервера, чтобы автоматически конфигурировать сертификат
CERT_CONFIG="listen 443 ssl; # managed by Certbot
  ssl_certificate \/etc\/letsencrypt\/live\/$DOMAIN\/fullchain.pem; # managed by Certbot
  ssl_certificate_key \/etc\/letsencrypt\/live\/$DOMAIN\/privkey.pem; # managed by Certbot
  include \/etc\/letsencrypt\/options-ssl-nginx.conf; # managed by Certbot
  ssl_dhparam \/etc\/letsencrypt\/ssl-dhparams.pem; # managed by Certbot
} server {
    if (\$host = $DOMAIN) {
        return 301 https:\/\/\$host\$request_uri;
    } # managed by Certbot

    listen 80;
    server_name $DOMAIN;
    return 404; # managed by Certbot
"

sed -i "s/# INSERT_CERT_CONFIG_HERE/$CERT_CONFIG/" "/etc/nginx/sites-available/$APP_NAME"
echo "Дебаг. Поменяли конфиг nginx.conf"

# Проверяем наличие cronjob для автоматического обновления
if ! crontab -l | grep -q "$CRONJOB_NAME"; then
    # cronjob нет, создаем новую
    echo "0 0 1 * * certbot renew" | crontab -
    echo "Создана cronjob для автоматического обновления сертификата."
else
    echo "cronjob для автоматического обновления уже существует."
fi