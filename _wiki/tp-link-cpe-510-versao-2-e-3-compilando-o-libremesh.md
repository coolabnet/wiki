---
title: "TP-Link CPE 510 Versão 2 e 3 - Compilando o LibreMesh"
layout: page
permalink: /tp-link-cpe-510-versao-2-e-3-compilando-o-libremesh/
---

Pacotes necessários: git,..

Vamos clonar o repositório para nossa máquina:
git clone https://github.com/LibreRouterOrg/openwrt.git

Entraremos no diretóŕio que acabamos de baixar:
cd librerouter/openwrt

Agora,vamos mudar de 'ramo': (saindo do 'master' para 'cpe510v2_v3)
git checkout cpe510v2_v3

Agora, existem várias configurações prontas, as quais estão no diretório 'configs':
cp configs/default_config .config

Podemos entrar no menu de configurações e escolher quais pacotes adicionais vamos querer utilizar, ou simplesmente executar o próximo comando:
make menuconfig

Ou, se desejarmos, podemos compilar direto:
make -j3 V=sc
(-j(numero de processadores + 1))

Após, poderemos encontrar os arquivos na pasta /bin/targets/ar71xx/generic.

Os arquivos que contém a palavra **factory** indica que a imagem deve ser utilizada em roteadores que contém o firmware **original** do fabricante.

Os que contém a palavra **sysupgrade** devem ser utilizados em roteadores que o firmware já foi modificado. Ou seja, que tenham o libremesh, openwrt, instalados.
