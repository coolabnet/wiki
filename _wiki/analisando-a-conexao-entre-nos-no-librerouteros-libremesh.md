---
title: "Analisando a conexão entre nós no librerouterOS/libremesh"
layout: page
permalink: /analisando-a-conexao-entre-nos-no-librerouteros-libremesh/
---

Nesse tutorial vamos aprender como analisar a conexão entre os nós em uma rede mesh baseada em Libremesh

1- Acesse o seu roteador por ssh:

`ssh root@thisnode.info`

2- Identifique a(s) interfaces mesh do seu dispositivo com o comando `iwinfo`

`root@conteiner-3500:~# iwinfo`

Você deve ter uma saida parecida com essa

```

wlan0-ap  ESSID: "PSP"
          Access Point: C4:6E:1F:08:83:CE
          Mode: Master  Channel: 11 (2.462 GHz)
          Tx-Power: 18 dBm  Link Quality: 70/70
          Signal: -39 dBm  Noise: -95 dBm
          Bit Rate: 65.0 MBit/s
          Encryption: none
          Type: nl80211  HW Mode(s): 802.11bgn
          Hardware: unknown [Generic MAC80211]
          TX power offset: unknown
          Frequency offset: unknown
          Supports VAPs: yes  PHY name: phy0

wlan0-apname ESSID: "PSP/conteiner-3500"
          Access Point: C6:6E:1F:08:83:CE
          Mode: Master  Channel: 11 (2.462 GHz)
          Tx-Power: 18 dBm  Link Quality: 56/70
          Signal: -54 dBm  Noise: -95 dBm
          Bit Rate: 60.1 MBit/s
          Encryption: none
          Type: nl80211  HW Mode(s): 802.11bgn
          Hardware: unknown [Generic MAC80211]
          TX power offset: unknown
          Frequency offset: unknown
          Supports VAPs: yes  PHY name: phy0

wlan1-mesh ESSID: "LiMe"
          Access Point: C4:6E:1F:08:83:CF
          Mode: Mesh Point  Channel: 48 (5.240 GHz)
          Tx-Power: 15 dBm  Link Quality: 26/70
          Signal: -84 dBm  Noise: -89 dBm
          Bit Rate: 6.5 MBit/s
          Encryption: unknown
          Type: nl80211  HW Mode(s): 802.11an
          Hardware: 168C:0033 168C:A120 [Atheros AR9580]
          TX power offset: none
          Frequency offset: none
          Supports VAPs: yes  PHY name: phy1
```

3- Nesse caso temos apenas uma interface de conexões na malha, `wlan1-mesh`. Para ver as conexões que `wlan1-mesh` está fazendo podemos usar o comando:

`root@conteiner-3500:~# iwinfo wlan1-mesh a | mac2bat`

```

interno_wlan1_mesh  -83 dBm / -90 dBm (SNR 7)  560 ms ago
	RX: 6.5 MBit/s, MCS 0, 20MHz                 2259598 Pkts.
	TX: 6.5 MBit/s, MCS 0, 20MHz                  637902 Pkts.
	expected throughput: unknown
```

4- Como podemos ver existe uma conexão com um `-83dbm`. Para analisar mais a fundo a troca de pacotes, podemos fazer:

`root@conteiner-3500:~# iw dev wlan1-mesh station dump | mac2bat`

```

Station interno_wlan1_mesh (on wlan1-mesh)
	inactive time:	25530 ms
	rx bytes:	451306605
	rx packets:	2259664
	tx bytes:	563626204
	tx packets:	637906
	tx retries:	394145
	tx failed:	3218
	rx drop misc:	207849
	signal:  	-85 [-87, -89] dBm
	signal avg:	-84 [-87, -87] dBm
	Toffset:	73017314608 us
	tx bitrate:	6.5 MBit/s MCS 0
	rx bitrate:	6.5 MBit/s MCS 0
	mesh llid:	49472
	mesh plid:	50510
	mesh plink:	ESTAB
	mesh local PS mode:	ACTIVE
	mesh peer PS mode:	ACTIVE
	mesh non-peer PS mode:	ACTIVE
	authorized:	yes
	authenticated:	yes
	associated:	yes
	preamble:	long
	WMM/WME:	yes
	MFP:		no
	TDLS peer:	no
	DTIM period:	2
	beacon interval:100
	short slot time:yes
	connected time:	94539 seconds
```

Devemos observar os valores `tx packets:	637906` e `tx retries:	394145` como o valor de *tx-packets* é muito maior que o *tx retries* podemos considerar que é uma conexão ruim mais num limite aceitável, pois ele ainda esta transmitindo mais do que retransmitindo.

Se o valor de retransmissão for maior do que o de transmissão tem uma coisa bem errada com essa conexão pois um roteador não deve passar a maior parte do tempo retransmitindo, isso é sinal de uma má configuração ou o [problema do nó oculto]({{ "/problema-do-no-oculto/" | relative_url }})

Uma métrica importante também é o survey, com ele podemos ver quanto tempo o radio esta ocupado e quanto tempo está transmitindo:

`root@quaresmeira2:~# iw wlan0-mesh survey dump`

```

Survey data from wlan0-mesh
	frequency:			2412 MHz
	noise:				-94 dBm
	channel active time:		74 ms
	channel busy time:		22 ms
	channel receive time:		22 ms
	channel transmit time:		0 ms
Survey data from wlan0-mesh
	frequency:			2417 MHz
Survey data from wlan0-mesh
	frequency:			2422 MHz
Survey data from wlan0-mesh
	frequency:			2427 MHz
Survey data from wlan0-mesh
	frequency:			2432 MHz
Survey data from wlan0-mesh
	frequency:			2437 MHz
Survey data from wlan0-mesh
	frequency:			2442 MHz
Survey data from wlan0-mesh
	frequency:			2447 MHz
Survey data from wlan0-mesh
	frequency:			2452 MHz
Survey data from wlan0-mesh
	frequency:			2457 MHz
Survey data from wlan0-mesh
	frequency:			2462 MHz
	noise:				-94 dBm
	channel active time:		79 ms
	channel busy time:		20 ms
	channel receive time:		19 ms
	channel transmit time:		0 ms
Survey data from wlan0-mesh
	frequency:			2467 MHz
Survey data from wlan0-mesh
	frequency:			2472 MHz [in use]
	noise:				-83 dBm
	channel active time:		844075 ms
	channel busy time:		171250 ms
	channel receive time:		156382 ms
	channel transmit time:		6001 ms
```

As várievies `channel active time` e `channel busy time` mostram respectivamente o tempo que o radio ficou ativo e ocupado.
