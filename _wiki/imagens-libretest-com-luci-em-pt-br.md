---
title: "Imagens LibreTest com Luci em pt br"
layout: page
permalink: /imagens-libretest-com-luci-em-pt-br/
---

1. Download de imagens prontas

Abaixo você encontra uma lista de **firmwares compilados** e prontos para uso em hardwares disponíveis no Brasil entre 2017 e 2019.

Essas imagens foram compiladas com base na **versão 18.06 do openwrt** do [git](https://github.com/LibreRouterOrg/openwrt) **librerouter** entre agosto e dezembro de 2019.

Essa compilação traz além do **default libre-router** (lime-app / firstbootwizard / pirania ) o ambiente gráfico **luci** em pt-br, a página **luci-status** para acesso a algumas informações do sistema sem a necessidade do usuário estar logado, a pagina  **luci-statistics**  que contem um sistema de coleta de dados mais avançada (collectd) e o pacote de acesso remoto **zerotier**, sendo que os ultimos dois vem desativados por padrão e necessitam de configuração manual assim como o portal captivo pirania.

Foram alterados também o comportamento padrão da versão em relação ao uso da malha, sendo adicionada  a função de executar a função de **mesh** em  **2.4Ghz** além do **5ghz** já ativo por padrão nessa versão.

O nome padrão desta rede é **libretest** e o nome do nodo ao iniciar é  **node-%M4%M5**, onde M4 e M5 são respectivos ao quarto e quinto par de endereços MAC, mas isso pode ser mudado ao iniciar o roteador em sua primeira conexão ao endereço http://thisnode.info.

  1. Tabela Hardware / Firmware

<table border="1"cellspacing="2">
 <tr>
  <th>Nome</th>
  <th>Modelo</th>
  <th>Versão</th>
  <th>Firmwares</th>
 </tr>
 <tr>
  <td>AC1200</td>
  <td align="center">C5</td>
  <td>1</td>
  <td>[zip](https://www.coolab.org/wp-content/uploads/2019/12/LiMe-LiRo-1806-LuciV-archer-c5-v1.zip) </td>
 </tr>
 <tr>
  <td>AC1750</td>
  <td align="center">Archer C7</td>
  <td>5</td>
  <td>zip ?</td>
 </tr>
 <tr>
  <td>N750</td>
  <td align="right">TL-WDR 4300</td>
  <td>1.7</td>
  <td>[zip](https://www.coolab.org/wp-content/uploads/2019/12/LiMe-LiRo-1806-LuciV-tl-wdr4300-v1.zip)</td>
 </tr>
 <tr>
  <td>CPE210</td>
  <td align="center">CPE210</td>
  <td>1 e 2</td>
  <td>zip ?</td>
 </tr>
 <tr>
  <td>CPE210</td>
  <td align="center">CPE210</td>
  <td>3</td>
  <td>[zip](https://www.coolab.org/wp-content/uploads/2019/12/LiMe-LiRo-1806-LuciV-cpe210-v3.zip)</td>
 </tr>
 <tr>
  <td>LibreRouter</td>
  <td align="center">LiRo</td>
  <td>1</td>
  <td>[zip](https://www.coolab.org/wp-content/uploads/2019/12/LiMe-LiRo-1806-LuciV-librerouter-v1.zip)</td>
 </tr>
 <tr>
  <td>3500</td>
  <td align="center">TL-WDR3500</td>
  <td>1</td>
  <td>[zip](https://www.coolab.org/wp-content/uploads/2019/12/LiMe-LiRo-1806-LuciV-tl-wdr3500-v1.zip)</td>
 </tr>
 <tr>
  <td>3600</td>
  <td align="center">TL-WDR3600</td>
  <td>1</td>
  <td>[zip](https://www.coolab.org/wp-content/uploads/2019/12/LiMe-LiRo-1806-LuciV-tl-wdr3600-v1.zip)</td>
 </tr>
</table>

  1. Configuração da compilação

Caso você queira compilar sua própria versão ou adicionar algum hardware a lista, o arquivo de configuração de comunidade que gerou esta imagem se encontra abaixo.
O procedimento deve ser clonar o git do projeto LibreRouter/openwrt e adicionar estas mudanças em files/etc/config/lime-community
Para os pacotes Luci, o processo de seleção foi por ambiente grafico, via make menuconfig eapós a seleção de luci, luci-mod-status e luci-app-statistics.

```
1. Read the documentation in /docs directory
1. and on http://libremesh.org

    1. System options

config lime system
	option hostname 'node-%M4%M5'

    1. Network general option

config lime network

    1. WiFi general options

config lime wifi
	list modes 'ap_2ghz'
	list modes 'apname_2ghz'
	list modes 'ieee80211s_2ghz'
	list modes 'ap_5ghz'
	list modes 'apname_5ghz'
	list modes 'ieee80211s_5ghz'
	option ap_ssid 'libretest'
	option apname_ssid 'libretest/%H'
	option adhoc_ssid 'LiMe.%H'
	option ieee80211s_mesh_id 'LiMe'

```

1. Versão sem adições e modificações

Caso você prefira uma versão pura do LibreMesh para librerouter em desenvolvimento atualmente (com malha  apenas na rede 5ghz e sem os pacotes luci), é só clonar o [git](https://github.com/LibreRouterOrg/openwrt) e seguir as instruções de compilação.
