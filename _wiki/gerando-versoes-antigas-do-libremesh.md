---
title: "Gerando versões antigas do Libremesh"
layout: page
permalink: /gerando-versoes-antigas-do-libremesh/
---

Muitas vezes temos que gerar versões antigas do Libremesh para que tenham compatibilidade com instalações de malhas que foram criadas com uma versão específica. Vamos fazer aqui uma versão de 2019, com openwrt/18,06 sem o lime-app, com protocolo mesh bmx6,

Para ver qual versão está sendo executada na rede, você olhar a página de status no http://thisnode.info. Mas nas versões mais recentes, com lime-app, essa informação não aparece, Portanto faça login por ssh e veja o texto que aparece logo após o login.

```

  _______                     ________        __
 |       |.-----.-----.-----.|  |  |  |.----.|  |_
 |   -   ||  _  |  -__|     ||  |  |  ||   _||   _|
 |_______||   __|_____|__|__||________||__|  |____|
          |__| W I R E L E S S   F R E E D O M
 -----------------------------------------------------
 OpenWrt 18.06.4, r7808-ef686b7292
 -----------------------------------------------------
  ___   __ __                _______             __
 |   |_|__|  |--.----.-----.|   |   |-----.-----|  |--.
 |     |  |  _  |   _|  -__||       |  -__|__ --|     |
 |_____|__|_____|__| |_____||__|_|__|_____|_____|__|__|

 ------------------------------------------------------
 LiMe master development (master rev. 2aabcf2 20191016_1027)
 ------------------------------------------------------
```

A melhor maneira de fazer isso é com o sdk do openwrt, adicionando os pacotes do Lime. Comece seguindo o tutorial do Lime que pode ser encontrado [aqui](https://libremesh.org/development.html). Você pode baixar a versão 18.06 do openwrt como eles sugerem, ou ser até mais específico e baixar um determinado tag. Os tags disponíveis podem ser vistos no [repositório](https://git.openwrt.org/?p=openwrt/openwrt.git;a=summary) do openwrt.

Em seguida, o tutorial do Lime explica como adicionar os pacotes ao arquivo feeds.conf do openwrt. Nessa etapa, também podem ser especificadas diferentes versões do Lime. Para baixar um tag, use um ponto-e-vírgula seguido do nome do tag. Para acessar um commit específico, você pode usar um circunflexo. Como o Lime não dá a informação do tag na tela inicial, usar o código hash do commit (2aabcf2 acima) pode ser uma opção. Exemplos:

```

src-git packages https://git.openwrt.org/feed/packages.git^5eb055306f
src-git luci https://git.openwrt.org/project/luci.git;openwrt-18.06
```

Para esse firmware, isso não foi necessário e o feeds.conf ficou assim:
```

src-git packages https://git.openwrt.org/feed/packages.git
src-git luci https://git.openwrt.org/project/luci.git;openwrt-18.06
src-git routing https://git.openwrt.org/feed/routing.git;openwrt-18.06
src-git telephony https://git.openwrt.org/feed/telephony.git;openwrt-18.06
src-git libremesh https://github.com/libremesh/lime-packages.git
src-git libremap https://github.com/libremesh/libremap-agent.git
```

Continuamos seguindo o tutorial até executar o **make menuconfig**. Como queremos usar bmx6, a seleção de pacotes será um pouco diferente do tutorial. Deselecione os pacotes que sugeridos, e selecione os seguintes dentro do **Lime**. Observe que a lime-app não é selecionada. Selecione primeiro o lime-proto-bmx6 para que o bmx6-auto-gw-mode aparece. Talvez alguns pacotes sejam desnecessários, quem souber, que nos corrija :)

```

  │ │                           -*- bandwidth-test................... Internet download bandwidth measurement                    │ │
  │ │                           <*> batman-adv-auto-gw-mode.. Set batman-adv gw_mode by internet availability                    │ │
  │ │                           <*> bmx6-auto-gw-mode..................... bmx6 auto Internet gateway module                     │ │
  │ │                           < > check-date-http.............. Keep local date under NTP too far away skew                    │ │
  │ │                           < > first-boot-wizard...................................... first-boot-wizard                    │ │
  │ │                           < > hotplug-initd-services................. Hotplug events of init.d services                    │ │
  │ │                           <*> lime-ap-watchping.. Watchping hooks to manage AP SSID if network problems                    │ │
  │ │                           < > lime-app......................................................... LimeApp                    │ │
  │ │                           <*> lime-debug......................................... libremesh debug utils                    │ │
  │ │                           <*> lime-hwd-ground-routing........... Manage 802.1q VLANs for ground routing                    │ │
  │ │                           <*> lime-hwd-openwrt-wan............ Respect openwrt wan interface as default                    │ │
  │ │                           < > lime-hwd-usbradio.............. LiMe hardware detection usb radio support                    │ │
  │ │                           <*> lime-map-agent....................................... LiMe LibreMap agent                    │ │
  │ │                           <*> lime-proto-anygw................................ LiMe anygw proto support                    │ │
  │ │                           <*> lime-proto-babeld.............................. LiMe babeld proto support                    │ │
  │ │                           <*> lime-proto-batadv.......................... LiMe batman-adv proto support                    │ │
  │ │                           < > lime-proto-bgp.................................... LiMe BGP proto support                    │ │
  │ │                           <*> lime-proto-bmx6.................................. LiMe Bmx6 proto support                    │ │
  │ │                           < > lime-proto-bmx7.................................. LiMe Bmx7 proto support                    │ │
  │ │                           < > lime-proto-olsr........................... LiMe OLSR proto support (IPv4)                    │ │
  │ │                           < > lime-proto-olsr2...................... LiMe OLSR2 proto support (IPv4/v6)                    │ │
  │ │                           < > lime-proto-olsr6.......................... LiMe OLSR proto support (IPv6)                    │ │
  │ │                           -*- lime-proto-wan.................................... LiMe wan proto support                    │ │
  │ │                           -*- lime-report.............................. LibreMesh status report utility                    │ │
  │ │                           <*> lime-smart-wifi................ Configure wifi mesh and ap hardware based                    │ │
  │ │                           -*- lime-system....................................... libremesh system files                    │ │
  │ │                           <*> lime-webui.................... libremesh web user interface based on LUCI  --->              │ │
  │ │                           -*- shared-state..................... Very minimal state sharing betwen nodes                    │ │
  │ │                           < >   shared-state-babeld_hosts........... babeld-hosts module for shared-state                  │ │
  │ │                           < >   shared-state-bat_hosts................. bat-hosts module for shared-state                  │ │
  │ │                           -*-   shared-state-dnsmasq_hosts......... dnsmasq hosts module for shared-state                  │ │
  │ │                           -*-   shared-state-dnsmasq_leases....... dnsmasq leases module for shared-state                  │ │
  │ │                           < >   shared-state-nodes_and_links..... nodes_and_links module for shared-state                  │ │
  │ │                           < >   shared-state-persist................ Persists shared-state in usb devices                  │ │
  │ │                           < >   shared-state-pirania............. Pirania vaucher module for shared-state
```

Além disso, selecionar LUCI -> Collections -> Luci. Salve as configurações e saia.

Agora é só rodar o make e pronto, já temos a versão  bmx6 do lime.
