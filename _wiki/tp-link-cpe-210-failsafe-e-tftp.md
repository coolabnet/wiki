---
title: "TP-Link CPE 210 FailSafe e TFTP"
layout: page
permalink: /tp-link-cpe-210-failsafe-e-tftp/
---

## TP-Link CPE 210 FailSafe e TFTP
Em caso de pŕoblemas com alguma gravação no cpe, precisaremos usar o modo de failsafe para executar nova gravação e restaurar o sistema, para isso precisamos seguir os seguintes passos:

para entrar em failsafe, desligar o roteador pelo cabo de rede, contar 5 segundos, colocar um pino em reset, ligar contando até 10, luz da lan deve ligar sem ter nada conectado nela...

assim que ela ligar colocar cabo da lan no roteador e na maquina, colocar a maquina local em ip 192.168.0.100/24 pois o roteador esta em 192.168.0.254. Isso pode ser feito de distintas maneiras, via terminal é aconselhado desligar o gerenciador de rede e após isso fixar o ip:

```
systemctl stop NetworkManager
```
e conferir com

```
systemctl status NetworkManager
● NetworkManager.service - Network Manager
Loaded: loaded (/usr/lib/systemd/system/NetworkManager.service; enabled; vendor preset: disabled)
 Drop-In: /usr/lib/systemd/system/NetworkManager.service.d
       └─NetworkManager-ovs.conf
 Active: inactive (dead) since Wed 2019-01-23 18:06:42 -02; 8s ago
```
após isso adicionar ip na interface

```
ip a add 192.168.0.100/24 dev enp5s0
```
conferir com tcpdump apontando para a interface local

```
tcpdump -nli enp5s0
```
`1280 ARP, Request who-has 192.168.0.254 tell 192.168.0.100, length 28 18:16:31.181334 ARP, Reply 192.168.0.254 is-at ba:be:fa:ce:08:41, length 46 18:16:32.462956 IP 192.168.0.254.3422 &gt; 192.168.0.100.69:  31 RRQ &quot;recovery.bin&quot; octet timeout 2 18:16:32.463009 IP 192.168.0.100 &gt; 192.168.0.254: ICMP 192.168.0.100 udp port 69 unreachable, length 67 18:16:35.663035 IP 192.168.0.254.3422 &gt; 192.168.0.100.69:  31 RRQ &quot;recovery.bin&quot; octet timeout 2 18:16:35.663100 IP 192.168.0.100 &gt; 192.168.0.254: ICMP 192.168.0.100 udp port 69 unreachable, length 67`

o failsafe esta pronto para pedir um arquivo por tftp para a maquina .100, por isso colocamos o ip antes, mas agora precisamos subir um servidor local e depois colocar o arquivo solicitado la dentro e também vemos que o roteador esta pedindo um arquivo chamado recovery.bin.

```
 # atftpd --daemon --bind-address 192.168.0.100 /tftpboot/
```
e os logs do journalctl:

```
jan 23 18:17:38 Darth atftpd[5947]: Advanced Trivial FTP server started (0.7.1)
jan 23 18:17:38 Darth atftpd[5948]: atftpd: can't bind port 192.168.0.100:69/udp
```
como user normal não deu certo, tentar como root:

```
$ atftpd --daemon --bind-address 192.168.0.100 /tftpboot/
```
e os logs:

```
jan 23 18:19:27 Darth atftpd[5979]: Advanced Trivial FTP server started (0.7.1)
jan 23 18:19:27 Darth sudo[5978]: pam_unix(sudo:session): session closed for user root
jan 23 18:19:27 Darth atftpd[5980]: atftpd: can't change identity to nobody.nogroup, exiting.
```
conferindo no sistema, vi que /etc/group não tinha o nogroup, criado:

```
groupadd nogroup
```
: Advanced Trivial FTP server started (0.7.1) jan 23 18:26:03 Darth sudo[6244]: pam_unix(sudo:session): session closed for user root jan 23 18:26:03 Darth atftpd[6248]: Serving recovery.bin to 192.168.0.254:3487

agora o servidor local ja reconhece a pasta e o roteador como cliente, precisamos mover o arquivo que usaremos para restaurar a imagem para a pasta que criamos:

o tcpdump esta mostrando que a busca do arquivo esta dando timeout: 18:28:46.456018 IP 192.168.0.254.1842 &gt; 192.168.0.100.69: 31 RRQ &quot;recovery.bin&quot; octet timeout 2 18:28:46.456311 IP 192.168.0.100.52866 &gt; 192.168.0.254.1842: UDP, length 19

copiar para a pasta o firmware versao factory, renomear para recovery.bin

18:42:34.859906 ARP, Request who-has 192.168.0.100 tell 192.168.0.254, length 46 18:42:34.859945 ARP, Reply 192.168.0.100 is-at 28:d2:44:2c:31:53, length 28 18:42:34.859998 IP 192.168.0.254.1878 &gt; 192.168.0.100.69: 31 RRQ &quot;recovery.bin&quot; octet timeout 2 18:42:34.860449 IP 192.168.0.100.33171 &gt; 192.168.0.254.1878: UDP, length 12 18:42:34.860516 IP 192.168.0.254.1878 &gt; 192.168.0.100.33171: UDP, length 4 18:42:34.860675 IP 192.168.0.100.33171 &gt; 192.168.0.254.1878: UDP, length 516

e ver o fluir da rede... o roteador vai reiniciar... reativar o networka managerr e receber ip via cabo!
