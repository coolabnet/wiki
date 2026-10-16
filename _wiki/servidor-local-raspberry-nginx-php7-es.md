---
title: "Servidor Local Raspberry + Nginx + PhP7/es"
layout: page
permalink: /servidor-local-raspberry-nginx-php7-es/
---

Tutorial de servidor local con Raspberry Pi

Necesidades

- RaspberryPi 3

- Fuente de 3A

- Cable ethernet

- Disco duro externo de 1Tb

- tarjeta de memoria

Instrucciones

- Para arrancar una raspberry pi, hay que instalar un sistema operativo en la tarjeta SD. Lo más sencillo es utilizar el sistema Raspbian Stretch Lite, que puedes obtener en:

```

https://www.raspberrypi.org/downloads/raspbian/
```

- En el enlace vas a descargar un archivo compactado en formato zip. En sistemas linux lo puedes expandir con el comando:

```

unzip 2019-07-10-raspbian-buster-lite.zip
```

- Los sistemas operativos deben ser escritos en la tarjeta - no es lo mismo que copiar y pegar. En una terminal, lo podemos hacer con el comando:

```

dd bs=4M if=22019-07-10-raspbian-buster-lite.img of=/dev/sdX conv=fsync
```

sdX es la partición de su tarjeta de memoria. Puedes ejecutar  `df -h` para saber cual es la partición.

- También se puede utilizar el aplicativo [| Etcher](https://www.balena.io/etcher/) para hacer lo mismo sin utilizar la terminal. En ese caso, no hace falta sin expandir el zip.

- Una vez que la tarjeta esté preparada, hay la posibilidad de no utilizar una pantalla para configurar el sistema. Para eso, hay que habilitar el acceso por SSH: introduzca la tarjeta en el lector y crie un archivo vacíon en la partición boot, llamado ssh.

```

sudo touch /media/USUARIO/boot/ssh
```

- Conecte la Raspberry por cable de red a su router y acceda a ella con el comando:

```

ssh pi@raspberrypi
```

Utilice la contraseña definida por defecto: raspberry.

  - Si por alguna eventualidad la raspi no funcione, con un error como "conection refused ... port 22", necesitarás conectarla a una pantalla, un teclado, y entrar con el comando:

```

rm /etc/ssh/ssh_host_*
dpkg-reconfigure openssh-server
```

- Conecte el disco duro USB y utilice el comando para ver donde se ha conectados (por ejemplo /dev/sda1)

```

df -h
```

- Cree la carpeta donde se montará el pendrive/disco duro

```

sudo mkdir hdexterno
sudo mount /dev/sda1 /media/hdexterno
```

- cree las carpetas para los contenidos

```

sudo mkdir /media/hdexterno/musicas
sudo mkdir /media/hdexterno/fotos
sudo mkdir /media/hdexterno/textos
sudo mkdir /media/hdexterno/fotos
```

- Actualice los repositorios

```

sudo apt update && sudo apt upgrade
```

- Ahora vamos a instalar los paquetes de software que se necesitarán

```

sudo apt-get install -y nginx
```

- Arranque el nginx

```

sudo /etc/init.d/nginx start
```

- Pruebe en tu navegador accedendo a la dirección

```

raspberrypi.lan
```

- Instale los paquetes de php7.0 y git

```

sudo apt-get install php-fpm git
```

- edite el archivo de configuración del nginx para conectarlo con el php

```

sudo nano /etc/nginx/sites-available/default
```

busque la línea

```

index index.html index.htm;
```

Añade a la línea la entrada `index.php` después de index

```

index index.php index.html index.htm;
```

Más abajo, busque la sección:

```

# pass the PHP scripts to FastCGI server listening on 127.0.0.1:9000
#
# location ~ \.php$ {
```

Borre `#` para que quede así:

```

 # pass the PHP scripts to FastCGI server listening on 127.0.0.1:9000
        #
        location ~ \.php$ {
                include snippets/fastcgi-php.conf;

        # With php-fpm (or other unix sockets):
        fastcgi_pass unix:/var/run/php/php7.0-fpm.sock;
        # With php-cgi (or other tcp sockets):
    #    fastcgi_pass 127.0.0.1:9000;
        }
```

En el bloque que pone `location ~ \` añade las líneas

Al final su archivo tiene que quedar así:

  1.
1. You should look at the following URL's in order to grasp a solid understanding
1. of Nginx configuration files in order to fully unleash the power of Nginx.
1. https://www.nginx.com/resources/wiki/start/
1. https://www.nginx.com/resources/wiki/start/topics/tutorials/config_pitfalls/
1. https://wiki.debian.org/Nginx/DirectoryStructure
1.
1. In most cases, administrators will remove this file from sites-enabled/ and
1. leave it as reference inside of sites-available where it will continue to be
1. updated by the nginx packaging team.
1.
1. This file will automatically load configuration files provided by other
1. applications, such as Drupal or Wordpress. These applications will be made
1. available underneath a path with that package name, such as /drupal8.
1.
1. Please see /usr/share/doc/nginx-doc/examples/ for more detailed examples.
  1.

1. Default server configuration
1.
server {
	listen 80 default_server;
	listen [::]:80 default_server;

	# SSL configuration
	#
	# listen 443 ssl default_server;
	# listen [::]:443 ssl default_server;
	#
	# Note: You should disable gzip for SSL traffic.
	# See: https://bugs.debian.org/773332
	#
	# Read up on ssl_ciphers to ensure a secure configuration.
	# See: https://bugs.debian.org/765782
	#
	# Self signed certs generated by the ssl-cert package
	# Don't use them in a production server!
	#
	# include snippets/snakeoil.conf;

	root /var/www/html;

	# Add index.php to the list if you are using PHP
	index index.php index.html index.htm index.nginx-debian.html;

	server_name _;

	location / {
		# First attempt to serve request as file, then
		# as directory, then fall back to displaying a 404.
		try_files $uri $uri/ =404;
	        autoindex on;
                autoindex_exact_size off;
	}

	# pass PHP scripts to FastCGI server
	#
	location ~ \.php$ {
		include snippets/fastcgi-php.conf;
	#
	#	# With php-fpm (or other unix sockets):
		fastcgi_pass unix:/run/php/php7.3-fpm.sock;
	#	# With php-cgi (or other tcp sockets):
	#	fastcgi_pass 127.0.0.1:9000;
	}

	# deny access to .htaccess files, if Apache's document root
	# concurs with nginx's one
	#
	#location ~ /\.ht {
	#	deny all;
	#}
}

1. Virtual Host configuration for example.com
1.
1. You can move that to a different file under sites-available/ and symlink that
1. to sites-enabled/ to enable it.
1.
1. server {
1. listen 80;
1. listen [::]:80;
1.
1. server_name example.com;
1.
1. root /var/www/example.com;
1. index index.html;
1.
1. location / {
1. try_files $uri $uri/ =404;
1. }
1. }

</pre>

Recargue el archivo de configuración con el comando:

```

sudo /etc/init.d/nginx reload
```

- Cree un archivo teste.php en la carpeta /var/www/html/ con el siguiente contenido:

```

<?php phpinfo(); ?>
```

- en tu navegador entre la dirección:

```

raspberry.lan/teste.php
```

- Si le sale una página con informaciones, todo ha funcionado bien. De lo contrario hubo algún error.

- Clonee el contenido del git en tu carpeta inicial

```

cd ~
git clone https://github.com/coolabnet/template_aldeia.git
```

- Edite con informaciones de tu comunidad y copie todo el contenido para tu carpeta web, y haga x usuarix www-data como owner de todo lo que está en la carpeta web para que se pueda enviar y descargar archivos

```

sudo cp -r ~/template_aldeia/* /var/www/html/
sudo chown -R www-data /var/www/html/*
```

- Revise el hostname ejecutando:

```

hostname -I
```

- Cambie el hostname de la raspberry

```

vim /etc/hostname
```

La dirección de tu servidor local será hostname.lan

- Para utilizar el disco duro para guardar el contenido del servidoe local, cree enlaces simbólicos dentro de la carpeta /var/www/html

```

cd /var/www/html
ln -s musicas /media/hdexterno/musicas/
ln -s videos /media/hdexterno/videos/
ln -s textos /media/hdexterno/textos/
ln -s fotos /media/hdexterno/fotos/
```

Acceda a tu servidor local y sea feliz!

Ref.

[https://www.raspberrypi.org/documentation/remote-access/web-server/nginx.md](https://www.raspberrypi.org/documentation/remote-access/web-server/nginx.md)
