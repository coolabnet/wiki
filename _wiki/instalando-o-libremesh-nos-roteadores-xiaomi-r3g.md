---
title: "Instalando o Libremesh nos roteadores Xiaomi R3G"
layout: page
permalink: /instalando-o-libremesh-nos-roteadores-xiaomi-r3g/
---

Enquanto o [Librerouter](https://www.librerouter.org) não fica pronto, nós sempre estamos procurando roteador compatíveis com o Libremesh para usar em nossas instalações. Os TP-LINK 4300/3500/3600, que eram nossos favoritos, já deixaram de ser fabricado há algum tempo. Mas a Xiaomi é uma faricante que tem apresentado alguns modelos compatíveis de boa qualidade.

O Xiaomi MIWIFI R3G tem dois rádios, uma boa potência e pode ser encontrado por bom preço no [aliexpress](https://es.aliexpress.com/item/4000028198844.html?spm=a2g0o.productlist.0.0.7462584f0EYaeY&algo_pvid=be3cf403-cbdc-422e-bddd-ffe52057e474&algo_expid=be3cf403-cbdc-422e-bddd-ffe52057e474-0&btsid=9833255a-36cc-4463-ba4b-416e32a32eaa&ws_ab_test=searchweb0_0,searchweb201602_6,searchweb201603_55).

A instalação nele é complicada mas tem dado sempre certo. Siga os passos abaixo (adaptados do https://openwrt.org/toh/xiaomi/mir3g#installation_via_ssh fórum do openwrt).:

1) Instalar um firmware "dev": http://bigota.miwifi.com/xiaoqiang/rom/r3g/miwifi_r3g_firmware_c2175_2.25.122.bin A aventura aqui é que os menus do roteador são todos em chinês...

- Conectar por cabo ao router. Conectar o router a internet por cabo wan. Ir ao endereço 192.168.31.1 (só funcionou com chrome). Clicar no texto em chinês abaixo à direita (hello).  Clicar no botão da próxima página (concordo). Criar uma senha na caixa de texto embaixo do texto Xiaomi_XXXX. Clicar no botão. Clicar no checkbox para que a senha admin seja a mesma senha que a do wifi. Clicar no botão (configuração concluida). Espere o reboot. Desconsidere as páginas depois do reboot.

- Ir novamente ao 192.168.31.1. Clique no botão. Clique no 3o. item do menu acima do desenho do roteador. Clique no botão com a letra i. Clique no botão cinza embaixo do botão azul (segundo da tela). Escolha o arquivo de  firmware. Aperte  o botão azul.  Deixe o checkbox sem clicar para manter a senha sem alterar. Clique no botão azul e espere o reboot.

2) Instalar o firmware com ssh
- Instalar o aplicativo mi router no celular. Crie a conta de usuário, caso não tenha.
- Conectar o celular no wifi do router e pareie o aplicativo com o qr code ou com a senha admin.
- Visite o endereço https://d.miwifi.com/rom/ssh e faça login com sua conta e senha.  Demora muito para conseguir entrar... um macete que funciona bem é escrever o https:// na barra de endereço sempre que não estiver aparecendo. Quando conseguir, baixe o arquivo clicando primeiro no botão ao lado do nome de sua rede (anote a senha de root que está à esquerda do botão!!), depois no botão a direita. É um bin que já vem com o ssh instalado com a senha de root que aparece ao lado do primeiro botão
- Formate um pen drive em FAT32 e copie o miwifi_ssh.bin para ele
- Desplugue o cabo de energia do roteador e insira o pen drive nele. Mantenha o botão de reset pressionado (com a ponta de clipe de papel ou algo assim) e plugue de volta o cabo de energia. Espere até o LED laranja começar a piscar, pode demorar um pouco. Depois que piscar, pode soltar o botão reset que o router vai rebootar em breve. Quando voltar a conectar, você já vai ter acesso ssh.

3) Instalar o firmware,finalmente!

- Baixar os arquivos de kernel e root: https://www.coolab.org/wp-content/uploads/2019/10/libremesh-ramips-mt7621-mir3g-squashfs-kernel1.bin e http://www.coolab.org/wp-content/uploads/2019/10/libremesh-ramips-mt7621-mir3g-squashfs-rootfs0.bin

- Caso prefira instalar o openwrt (que não faz mesh mas é um excelente firmware) use esses arquivos aqui http://downloads.openwrt.org/releases/18.06.4/targets/ramips/mt7621/openwrt-18.06.4-ramips-mt7621-mir3g-squashfs-kernel1.bin e http://downloads.openwrt.org/releases/18.06.4/targets/ramips/mt7621/openwrt-18.06.4-ramips-mt7621-mir3g-squashfs-rootfs0.bin

- Copie esses arquivos por ssh:  entre pelo terminal do diretório no seu computador onde estão os arquivos e use o comando
	```

scp ./libremesh-ramips-mt7621-mir3g-squashfs-kernel1.bin root@192.168.31.1:/tmp
scp ./libremesh-ramips-mt7621-mir3g-squashfs-rootfs0.bin  root@192.168.31.1:/tmp
```

- Se for instalar o openwrt, os arquivos são outros:
	```

scp ./openwrt-18.06.2-ramips-mt7621-mir3g-squashfs-kernel1.bin root@192.168.31.1:/tmp
scp ./openwrt-18.06.2-ramips-mt7621-mir3g-squashfs-rootfs0.bin  root@192.168.31.1:/tmp
```

- Entre por ssh no router: ssh root@192.168.31.1 *usando a senha que você anotou no passo 2.3 acima
- Use os comandos (para Libremesh):

```

mtd write /tmp/libremesh-ramips-mt7621-mir3g-squashfs-kernel1.bin kernel1
mtd write /tmp/libremesh-ramips-mt7621-mir3g-squashfs-rootfs0.bin rootfs0
nvram set flag_try_sys1_failed=1
nvram commit
reboot
```

- Para openwrt, os arquivos são outros. Use:

```

mtd write /tmp/openwrt-18.06.2-ramips-mt7621-mir3g-squashfs-kernel1.bin kernel1
mtd write /tmp/openwrt-18.06.2-ramips-mt7621-mir3g-squashfs-rootfs0.bin rootfs0
nvram set flag_try_sys1_failed=1
nvram commit
reboot
```

4) Pronto! Para configurar o Libremesh, conecte ao router, abra seu browser e visite a URL http://thisnode.info. Caso tenha instalado o OpenWrt lembre que ele não vem com wifi ligado por padrão, portanto conecte por cabo e entre no menu luci http://192.168.1.1 para ativar o wifi
