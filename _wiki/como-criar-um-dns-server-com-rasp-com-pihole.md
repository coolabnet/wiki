---
title: "Como criar um dns server com rasp com PiHole"
layout: page
permalink: /como-criar-um-dns-server-com-rasp-com-pihole/
---

# Como ter um filtro de DNS com PiHole no LibreMesh
O Pi-hole funciona como um filtro de DNS que protege seus dispositivos contra conteúdo indesejado, e o melhor sem instalar nenhum software do lado do cliente.
Esse tutorial tem o objetivo de mostra como fazer isso para usuários de redes com Libremesh.

## Instalando o Pi-Hole
Primeiro vamos precisar de uma raspberry com um dos sistemas suportados pelo [piHole](https://pi-hole.net)

Aqui vamos usar o [raspbian](https://www.raspberrypi.org/downloads/raspbian/), e um truque que te ajuda a econimizar muito tempo para instalar qualquer tipo de serviço na rasp sem ter que conecta-la a uma tela para configurações iniciais, é simplesmente colocar um arquivo vazio na particão boot chamado ssh. Com isso você pode ligá-la diretamente a um cabo ethernet no seu roteador e ela vai iniciar e ganhar um ip da rede que você pode conferir assim

-Entre por ssh no seu roteador
```

ssh root@IPDogateway
```

-veja quem está conectado fazendo
```

cat /tmp/dhcp.leases
```

você vai ver uma lista com três colunas, na terceira coluna o ip que estiver seguido por raspeberrypi guarde esse numero.

-entre na rasp por ssh usando o hostname da rasp ou o ip:
```

ssh pi@raspberrypi
```

-dentro do terminal da rasp faça
```

passwd
```
configure sua senha.

-para instalar o piHole faça:
```

curl -ksSL https://install.pi-hole.net | bash
```

Alternativamente você pode instalar via github

```

git clone --depth 1 https://github.com/pi-hole/pi-hole.git Pi-hole
cd "Pi-hole/automated install/"
sudo bash basic-install.sh
```

Ou alternativamente ao alternativo, você pode fazer:

```

wget -O basic-install.sh https://install.pi-hole.net
sudo bash basic-install.sh
```

Vai haver uma tentativa de autoconfiguração do sistema e algumas perguntas se deseja instalar o ambiente gráfico, confirme e prossiga.

pronto pi-Hole instalado, você pode conferir em /etc/pihole/install.log o log da instalação.

## Testando o PiHole solo
- no terminal de sua maquina, use o comando drill ou dig com o resolvedor apontado para o ip de seu raspie instalado:

```

drill google.com.br @ip.raspie
```
ou
```

dig terra.com.br @ip.raspie
```

Você deve receber algo assim
```

;; ->>HEADER<<- opcode: QUERY, rcode: NOERROR, id: 56549
;; flags: qr rd ra ; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 0
;; QUESTION SECTION:
;; google.com.br.  IN  A

;; ANSWER SECTION:
google.com.br.  299  IN  A  172.217.29.195

;; AUTHORITY SECTION:

;; ADDITIONAL SECTION:

;; Query time: 59 msec
;; SERVER: 10.65.202.161
;; WHEN: Tue Sep 18 10:13:20 2018
;; MSG SIZE  rcvd: 47
```

Caso voce receba os endereços perguntados (;; ANSWER SECTION: google.com.br. 299  IN  A  172.217.29.195) significa que seu pihole (;; Query time: 59 msec ;; SERVER: 10.65.202.161) esta respondendo as questoes DNS, agora voce pode configurar seu roteador para que todos na rede sejam contemplados de forma transparente,

Caso queira executar mais testes e ver ele em ambiente grafico em sua maquina, alterar o resolv.conf para que o endereço de servidor dns de sua maquina seja o proprio raspie, assim a navegação ja deve vir sem a publicidade.

# Configurando o PiHole no Libremesh
-No terminal do roteador edite o arquivo de configuração do lime com o seu editor de preferência

```

vim /etc/config/lime-community
```
Na secção *config lime 'network*' vá até a linha *list resolvers* e coloque o ip da rasp e salve o arquivo

-para as alterações começarem a valer faça
```

lime-config && lime-apply
```

-Entre na interface gráfica para ver os gráficos e tudo funcionando

```

http://IPdaRasp/adimin
```
