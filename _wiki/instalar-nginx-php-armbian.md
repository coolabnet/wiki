---
title: "Instalar Nginx PHP Armbian"
layout: page
permalink: /instalar-nginx-php-armbian/
---

**Versão do Debian: 9 (stretch)**

## Atualizar lista de pacotes do debian
```
sudo apt update
```

## Instalar Nginx
```
sudo apt install nginx
```

## Testar Nginx
Acessar no navegador o endereço do armbian

## Instalar php7 para nginx (php-fpm)
```
sudo apt install php-fpm
```

## Habilitar Nginx para acessar php:
Editar arquivo /etc/nginx/sites-available/default  (sudo nano /etc/nginx/sites-available/default)

Descomentar Linhas referente ao php fastcgi e ao htaccess, de modo que o arquivo fique com as seguintes linhas descomentadas:

```

server {
    listen 80 default_server;
    listen [::]:80 default_server;

    root /var/www/html;
    index index.php index.html index.htm index.nginx-debian.html;

    server_name your_server_ip;

    location / {
        try_files $uri $uri/ =404;
    }

    location ~ \.php$ {
        include snippets/fastcgi-php.conf;
        fastcgi_pass unix:/var/run/php5-fpm.sock;
    }

    location ~ /\.ht {
        deny all;
    }
}
```

## Reiniciar nginx:
```
sudo systemctl reload nginx
```

## Criar página de teste para verificar se php está rodando:
```
sudo nano /var/www/html/teste.php
```

 Inserir o seguinte código

```

<?php
    phpinfo();
?>
```

Acessar no navegador o endereço do armbian com o caminho para teste.php (se o nome do equipamento for amlogic, ficaria algo como: armbian.lan/teste.php)
Você deve visualizar a página de informações do php

## Fonte
Adaptado do tutorial: https://www.digitalocean.com/community/tutorials/how-to-install-linux-nginx-mysql-php-lemp-stack-on-debian-8
