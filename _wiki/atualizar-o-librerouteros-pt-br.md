---
title: "Atualizar o LibreRouterOS/pt-br"
layout: page
permalink: /atualizar-o-librerouteros-pt-br/
---

1. Instruções para Upgrade

1 - Baixe o release `xxx-sysupgrade.bin`

 1.1 - verifique o sha256!: `sha256sum xxx-sysupgrade.bin` e compare com a saída no fundo
 1.2 - copiar o arquivo para o roteador: `# scp librerouteros-v1.2-librerouter-lr1-sysupgrade.bin thisnode.info:/tmp/`

2 - Acesse o Roteador

 2.1 - Abra um terminal, digite `ssh root@thisnode.info`
 2.1 - Para instalar: `# safe-upgrade upgrade -n /tmp/librerouteros-v1.2-librerouter-lr1-sysupgrade.bin`
 2.2 - Para reiniciar: `# reboot`
 2.3 - Aguarde 5 minutos ou até você obter novamente um IP do roteador
 2.4 - Confirme a alteração: `ssh root@thisnode.info safe-upgrade confirm`

Leia [https://github.com/libremesh/lime-packages/blob/master/packages/safe-upgrade/Readme.md](https://github.com/libremesh/lime-packages/blob/master/packages/safe-upgrade/Readme.md) para mais detalhes usando safe-upgrade

  1. Download

- [librerouteros-v1.2-librerouter-lr1-sysupgrade.bin](https://gitlab.com/librerouter/openwrt/uploads/e4faf2ba15e9103e63d9e0255d42660e/librerouteros-v1.2-librerouter-lr1-sysupgrade.bin)

  1. Pacotes e outros binários

[RepoLibreRouterOs](http://repo.libremesh.org/librerouteros/v1.2/)

[Originalmente no gitlab](https://gitlab.com/librerouter/openwrt/-/releases/v1.2)
