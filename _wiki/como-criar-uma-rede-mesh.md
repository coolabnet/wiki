---
title: "Como criar uma rede mesh"
layout: page
permalink: /como-criar-uma-rede-mesh/
---

Por diversos motivos, a Coolab utiliza para distribuir o sinal em comunidades redes em malha com o firmware LibreMesh.

Nesse tutorial, vamos instalar esse firmware em um roteador TP-LINK WDR-3500. O ideal na verdade é ter mais de um roteador para ver a rede funcionando na prática.

## Conseguindo o firmware
O firmware nada mais é do que uma versão do linux especial para dispositivos portáteis (roteadores, por exemplo). A LibreMesh é baseada na distribuição de linux OpenWRT[http://openwrt.org/](http://openwrt.org/).

Existem diversas maneiras de conseguir o firmware: baixando uma imagem apropriada para seu roteador [daqui](http://builds.libremesh.org/current/targets/ar71xx/generic/), compilando o código fonte, ou, a nossa preferida, que é usar o cozinheiro de firmwares do projeto LibreMesh: http://chef.libremesh.org/

Crie uma conta lá. Se você souber trabalhar com chaves SSH, pode subir a sua; do contrário não se preocupe com isso. Crie uma nova rede, completando os parâmetros mínimos. O nome é muito importante, porque ele é que vai ser o nome do wifi da sua rede (o SSID). Coloque seu próprio usuário como admin.

Clique em create firmware profile. Caso queira que sua chave SSH seja incluída no firmware para acesso mais rápido, cheque a caixinha correspondente. Deixe o resto todo no default, e escolha as caixinhas dos modelos de roteadores que vai usar - no nosso caso o primeiro, TP-LINK TL-WDR3500/3600/4300/4310. Clique em create, e na página seguinte escolha "cook", e na seguinte "cook" novamente. Aguarde a resposta por mail ou na própria página.

Quando estiver pronto, clique em "download firmware" e encontre o modelo do seu roteador que termina em "-factory.bin". O "-sysupgrade" é para o caso em que você já tem o openwrt instalado. Baixe o arquivo para o seu computador.

## Instalando o firmware
Conecte o roteador ao seu computador através de um cabo de rede ligado em uma das portas amarelas (LAN). Desligue temporariamente seu wifi. Abra uma aba do seu navegador e entre no endereço 192.168.1.1, usando o usuário admin e a senha admin. Procure o menu sistema, e a opção upgrade firmware. Antes de subir o firmware para o roteador, renomeie o arquivo para algo mais curto, como wp3500.bin. Tente fazer o upgrade.

Caso você receba uma mensagem de erro, é provável que você tenha uma versão de equipamento que exige fazer algumas etapas a mais, para mudar o firmware original para uma versão mais antiga do próprio fabricante.
- Primeiro, baixe o firmmware dd-wrt nesse [link](ftp://ftp.dd-wrt.com/betas/2014/05-23-2014-r24118/tplink_tl-wdr3500v1/factory-to-ddwrt.bin)
- Em seguida, baixe o firmware original da tp-link em versão mais antiga [aqui](http://www.dd-wrt.com/phpBB2/download.php?id=30564). Você tem que estar logado no [fórum](http://www.dd-wrt.com/phpBB2/) do dd-wrt para baixá-lo, ou procurar o arquivo tl_wdr3500v1_webrevert.bin em outro lugar.
- Use o arquivo factory-to-ddwrt.bin (mude o  nome se for necessário). Espere o reboot. Desplugue e plugue o cabo de rede novamente, e entre no endereço 192.168.0.1. Procure a opção de upgrade de software no dd-wrt, e faça upgrade com o arquivo tl_wdr3500v1_webrevert.bin.
- Espere o reboot, desplugue e plugue o cabo novamente. Agora, finalmente, você pode instalar o firmware do libremesh.

## Usando o LibreMesh
Uma vez que o roteador ligue, ele anuncia a rede wifi pelo nome que foi definido no Chef. Conecte-se e se familiarize com os menus (são parecidos com os do OpenWrt). Para entrar na página do roteador, use o endereço http://thisnode.info/

Além dessa rede, é criada uma rede NomeDaSuaRede/NomedoDispositivo, e mais uma rede adhoc chamada LiMe, que faz as conexões entre os roteadores. Como esse roteador é dual band, as mesmas redes estarão duplicadas nas duas bandas. Caso você tenha flasheado mais de um roteador com LibreMesh, pode entrar no menu Graphic e ver com a rede mesh se forma automaticamente.

Clique em Administration, no fim da página, para ver todos os menus. Se você criar uma senha de admin, o acesso root por ssh será liberado. Para criar uma senha de wifi, você pode usar o menu WiFi e acessar as preferências das redes citadas acima.

## Conectando à Internet
Finalmente, para que sua rede mesh tenha acesso à Internet, basta plugar um cabo de rede na porta azul de qualquer roteador que esteja flasheado. Além disso, se você conectar em mais de um roteador, a rede vai escolher o melhor caminho para a Internet. Existe também a possibilidade de se conectar a um rede wifi. Em breve faremos novo tutorial para falar disso!
