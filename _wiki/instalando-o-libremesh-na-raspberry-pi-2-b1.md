---
title: "Instalando o Libremesh na Raspberry PI 2 B1"
layout: page
permalink: /instalando-o-libremesh-na-raspberry-pi-2-b1/
---

Com a imagem em seu computador, compilada ou baixada do site, execute os seguintes comandos para copiar a imagem para o cartão de memória:

Descobrindo onde o cartão de memória foi montado:
mount

Ao inserir o cartão de memória no computador, ele será 'montado'. Precisamos desmontá-lo antes de copiar a imagem para ele. Na linha de comando, digite:
umount /dev/mmcblk0

cat /home/darth/openwrt/bin/targets/brcm2708/bcm2709/openwrt-brcm2708-bcm2709-rpi-2-ext4-factory.img.gz | gunzip | sudo dd of=/dev/mmcblk0 bs=2M conv=fsync

**Observações**
A raspberry contém apenas uma interface ethernet. Com o LibreMesh instalado, ela funcionará como uma porta LAN. Ou seja, se plugar um computador, ele receberá um endereço IP.

**Adicionando outra interface**
