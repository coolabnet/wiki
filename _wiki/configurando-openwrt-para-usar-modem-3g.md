---
title: "Configurando OpenWRT para usar modem 3G"
layout: page
permalink: /configurando-openwrt-para-usar-modem-3g/
---

Por padrão, o OpenWRT não vem com suporte para modem 3G. Caso queira compartilhar a internet de um um modem assim em um roteador com OpenWRT, precisará fazer algumas configurações antes.

Verifique qual o driver que o USB modem (dongle) usa, nesse exemplo usaremos um dongle que tem suporte para o driver **cdc_ether** para compartilhar a internet. [Aqui](https://openwrt.org/docs/guide-user/network/wan/wwan/start) você encontrá ajuda para modems com outros tipos de drivers.

### Pacotes necessários
Antes de conectar o USB ao roteador, precisamos instalar alguns pacotes. Isso pode ser feito pela interface do roteador, Luci → System → Software ou através do terminal de comandos:
  root@cajita.lan:~# opkg install kmod-usb-net-cdc-ether usb-modeswitch

Se a instalação foi um sucesso, conecte o USB ao roteador e verifique o que o **dmesg** diz.
  root@cajita.lan:~# dmesg
  [   11.070592] usb 1-1: new high-speed USB device number 3 using ehci-platform
  [   11.092614] usbcore: registered new interface driver cdc_ether
  [   11.545401] cdc_ether 1-1:1.0 eth1: register 'cdc_ether' at usb-ehci-platform-1, CDC Ethernet Device, 00:1e:10:1f:00:00

No nosso exemplo, assim que o USB foi conectado, uma nova interface chamada **eth1** foi criada.

### Configurando a rede
Para finalizar, precisamos criar uma interface de rede que compartilhe a internet do modem 3G.
Isso pode ser feito através da Luci, Network → Interfaces → Add new interface… onde:

**General Setup**
Protocol: DHCP client
Hostname: cajita (você escolhe o nome que quiser)

**Physical Settings**

- Bridge interfaces
:- Selecione essa opção

- Interface: (selecione)
:- Ethernet Adapter: "eth1"
:- Wireless Network

ou através do terminal de comandos:
  root@cajita.lan:~# vi /etc/config/network
  config interface 'wanb'
	option proto 'dhcp'
	option metric '100'
	option type 'bridge'
	option _orig_ifname 'eth1'
	option _orig_bridge 'true'
	option ifname 'eth1 wan0'
