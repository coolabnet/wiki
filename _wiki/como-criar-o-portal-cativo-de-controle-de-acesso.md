---
title: "Como criar o portal cativo de controle de acesso"
layout: page
permalink: /como-criar-o-portal-cativo-de-controle-de-acesso/
---

**Informações preliminares**
- Essas instruções são para o roteador que está conectado à internet, fornecendo para o resto da rede. Não foi testado com mais de um gateway de saída para internet.
- Esse sistema de validação e portal cativo não funciona quando não há acesso à internet, ou quando o acesso cai. Para isso, tem uma gambiarra descrita no fim da página

## Para versão DaybootRely da LibreMesh (1706)
0. Esse tutorial supõe que você sabe usar o comando vi para editar texto em arquivos que estão no roteador. Se você sabe usar o comando scp também pode editar no seu PC e subir os arquivos editados para o seu roteador.

1. Faça o login na linha de comando via SSH e atualize os repositórios do roteador que receberá o portal captivo:

`opkg update`

2. Vamos agora instalar o [nodogsplash](http://nodogsplash.readthedocs.io/en/latest/).
Esté um pacote com as mudanças necessárias para instalar o captivo na versão 17.

`opkg install http://nuvem.tk/files/nodogsplash_0.9.2-1_mips_24kc.ipk`

3. Agora vamos editar o arquivo de configuração

`vi /etc/config/nodogsplash`

Neste arquivo, altere o arquivo nas seguintes linhas, de modo que se registre os seguintes parâmetros:

Altere o valor do "option enable" de 0 para 1

`option enable 1`

Descomentar (apagar o jogo da velha do início da linha) a linha a seguir:

`option config '/etc/nodogsplash/nodogsplash.conf'`

5. apague tudo que vem depois dessa linha

6. Agora salve o arquivo e saia do editor de texto.

7. Crie o arquivo /etc/nodogsplash/nodogsplash.conf pelo listado abaixo (fazendo as devidas modificações nos IP e página de redirecionamento). O IP a ser usado é o do menu network -> interfaces, interface LAN (IPV4) (sem o /16). O range são os dois primeiros números, seguidos de .0.0/16. (ex se o ip é 10.7.255.50, o range é 10.7.0.0/16.

```

GatewayInterface br-lan
GatewayInterfaceExtra bmx+
GatewayInterfaceExtra2 anygw

FirewallRuleSet authenticated-users {
     FirewallRule allow to 0.0.0.0/0
}

FirewallRuleSet users-to-router {
 # Nodogsplash automatically allows tcp to GatewayPort,
 # at GatewayAddress, to serve the splash page.
 # However you may want to open up other ports, e.g.
 # 53 for DNS and 67 for DHCP if the router itself is
 # providing these services.
    FirewallRule allow udp port 53530
    FirewallRule allow tcp port 53530
    FirewallRule allow udp port 67
 # You may want to allow ssh, http, and https to the router
 # for administration from the GatewayInterface.  If not,
 # comment these out.
    FirewallRule allow tcp port 22
    FirewallRule allow tcp port 80
    FirewallRule allow tcp port 443

}
# end FirewallRuleSet users-to-router

FirewallRuleSet preauthenticated-users {
 # For preauthenticated users to resolve IP addresses in their initial
 # request not using the router itself as a DNS server,
 # you probably want to allow port 53 udp and tcp for DNS.
    FirewallRule allow tcp port 53
    FirewallRule allow udp port 53
 # For splash page content not hosted on the router, you
 # will want to allow port 80 tcp to the remote host here.
 # Doing so circumvents the usual capture and redirect of
 # any port 80 request to this remote host.
 # Note that the remote host's numerical IP address must be known
 # and used here.

     #change the IP for the address of the gateway router
     FirewallRule allow tcp port 80 to 10.7.122.55

}
# end FirewallRuleSet preauthenticated-users

EmptyRuleSetPolicy preauthenticated-users passthrough
EmptyRuleSetPolicy users-to-router passthrough

#change the IP for the address of the gateway router
GatewayName 10.7.122.55:80

#GatewayPort 80

MaxClients 500

ClientIdleTimeout 720

ClientForceTimeout 14400

#change the range for the ip range of your mesh network
GatewayIPRange 10.7.0.0/16

BinVoucher "vale.sh"

ForceVoucher yes

EnablePreAuth yes
```

NÃO ESQUEÇA DE TROCAR OS IPs no arquivo acima!

8. Vá no menu system -> startup e confira se o nodogsplash está como ENABLED

9. Crie um arquivo chamado /etc/dnsmasq2 com o seguinte conteúdo. Novamente, troque o ip abaixo pelo o mesmo usado acima, do seu roteador

```

# auto-generated config file from /etc/config/dhcp
domain=lan
address=/#/10.7.122.55:2050/nodogsplash_auth/
addn-hosts=/tmp/hosts
user=dnsmasq
group=dnsmasq
port=53530
```

10. Edite o arquivo /etc/rc.local adicionando as seguintes linhas antes da linha "exit 0" (sem apagá-la). Troque novamente o ip.

```

/usr/sbin/dnsmasq -C /etc/dnsmasq2

((sleep 60; \
iptables -t nat -I ndsOUT 3 -p udp -m udp --dport 53 -j DNAT --to-destination 10.7.122.55:53530 ; \
iptables -t nat -I ndsOUT 4 -p tcp -m tcp --dport 53 -j DNAT --to-destination 10.7.122.55:53530 )&)

exit 0
```

11.Reinicie o roteador fisicamente ou usando o comando reboot.

12. Verifique se deu tudo certo até aqui procurando pelo processo do dnsmasq2

```

ps | grep dns
```

Você deve ver algo parecido com:
```

 1049 dnsmasq   1084 S    /usr/sbin/dnsmasq -C /etc/dnsmasq2
 2296 dnsmasq   1128 S    /usr/sbin/dnsmasq -C /var/etc/dnsmasq.conf.cfg02411c
 2297 root      1080 S    /usr/sbin/dnsmasq -C /var/etc/dnsmasq.conf.cfg02411c
29211 root      1184 S    grep dns
```

## Configurando o voucher
1. Conectando via SSH no roteador, vamos atualizar os repositórios e instalar o pacote do voucher
```

opkg update && opkg install http://nuvem.tk/files/vale_0.1-1_mips_24kc.ipk
```

2. Vamos renomear o arquivo HTML do splash
```

mv /etc/nodogsplash/htdocs/splash-vale.html /etc/nodogsplash/htdocs/splash.html
```

3. Reinicie o nodogpslash
```

/etc/init.d/nodogsplash restart
```

4. Traduza ou customize as mensagens de erro que estão no arquivo /www/cgi-bin/vale

5. Adicione seus códigos de VOUCHER no arquivo /etc/nodogsplash/vale/db.csv (se preferir, use um [gerador aletório](http://generator.voucherify.io/#)).

Veja um exemplo do arquivo [db.csv](https://github.com/coolabnet/lime-packages/blob/develop/packages/vale/files/etc/nodogsplash/vale/db.csv)

A primeira coluna não é utilizada. Cada linha tem que terminar com as duas vírgulas, sem espaços. As outras colunas serão usadas para anotar a hora e o MAC de cada conexão/voucher. Para gerar automaticamente as duas vírgulas ao fim de cada linha preencha a primeira linha. Exemplo:

```

code,field1,field2
6XvMcaLb,,
cF6m7eXu,,
nNqsSMCS,,
GSYJPotH,,
PecFaM8c,,
Tx2GgNNX,,
zEeTmcwu,,
hBg5858g,,
rmsgUqR2,,
```

6. Agora, copie o arquivo para o seu roteador

```
 scp db.csv root@thisnode.info:/etc/nodogsplash/vale/
```

## Customizando o portal captivo
1.

**Referências**

- [Tutorial da Nuvem](http://nuvem.tk/wiki/index.php/Fuma%C3%A7a_Data_Springs/Anexo_t%C3%A9cnico#Instala.C3.A7.C3.A3o_do_portal_de_controle_de_acesso)
- [Nodogsplash - Documentação](http://nodogsplash.readthedocs.io/en/latest/)
