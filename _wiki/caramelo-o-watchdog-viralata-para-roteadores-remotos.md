---
title: "Caramelo, o watchdog viralata para roteadores remotos"
layout: page
permalink: /caramelo-o-watchdog-viralata-para-roteadores-remotos/
---

<img src="{{ "/images/1/12/Viralata_caramelo.jpeg" | relative_url }}" alt="Viralata caramelo.jpeg">

A ideia desse projeto é criar um dispositivo que reinicia um roteador caso se perca o acesso a internet, desligando a eletricidade do aparelho e ligando de novo. A conexão é checada pelo wifi, portanto o roteador precisa tem um ponto de acesso, e precisamos da senha do wifi caso tenha alguma.

Existem duas possibilidades de equipamentos: uma a placa ESP8266, que tem mais recursos, e outra com a placa ESP-01, que é uma versao simplificada do mesmo chip. Essa versão é bem mais barata e simples de mexer, portanto só recomendamos usar o tutorial da ESP8266 se quiser fazer alguma coisa a mais com o projeto (como usar uma tela de display, ou algum sensor analógico).

- Versão com [ESP8266]({{ "/caramelo-com-esp8266/" | relative_url }}) (para criar novas utilidades)
- Versão com [ESP-01]({{ "/caramelo-com-esp01/" | relative_url }}) (recomendada)

Se encontrar qualquer problema ou tiver sugestões, abra um [issue](https://gitlab.com/coletivo-coolab/caramelo/-/issues) no nosso gitlab.

<figure><img src="{{ "/images/0/0d/ESP-01_com_relé_e_fios.jpeg" | relative_url }}" alt="Chip com relé"><figcaption>Chip com relé</figcaption></figure>
