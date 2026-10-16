---
title: "Como usar túneis ssh para administrar uma rede à distância usando OpenWrt ou LibreMesh"
layout: page
permalink: /como-usar-tuneis-ssh-para-administrar-uma-rede-a-distancia-usando-openwrt-ou-libremesh/
---

Muitas vezes criamos redes que estão expostas à Internet através de ip dinâmicos, ou mesmo com roteadores que não podem ser configurados. Assim é muito difícil entrar em um roteador dentro dessa rede se você não tem acesso físico ao aparelho.

Para acessar essas redes de fora existem algumas soluções como direcionar o tráfego da rede através de [vpn](http://www.brunovianna.net/documenta/?p=93) ou até serviços freemium como o [ngrok](http://ngrok).

A solução que vamos tratar aqui usa um pacote do [OpenWrt](http://openwrt.org) chamada sshtunnel, que instala os túneis como um serviço permanente. Para usá-la, você precisa de acesso root a um servidor na Internet e saber um pouco de como usar chaves ssh com par de chaves. Além disso, você precisa de um roteador com 8Mb para instalar os pacotes necessários.

## Engenharia de túneis
Em primeiro lugar, entre no seu roteador pela interface www. Crie uma senha de root, caso ainda não tenha sido criada. Instale os pacotes sshtunnel e openssh-keygen pelo menu system->software (atualize a lista de software antes de instalar). Você também pode instalá-los pela linha de comando:

```

opkg update
opkg install sshtunnel
opkg install openssh-keygen
```

Entre como root por ssh no seu roteador (caso ainda esteja na interface gráfica) e dê o seguinte comando, usando enter quando perguntado se quer criar senha (não crie) :

```

ssh-keygen -t rsa -f /root/.ssh/id_rsa
```

Ele vai gerar, dentro do diretório /root/.ssh dois arquivos: a chave privada **id_rsa** (que tem que ficar bem guardada) e a chave pública **id_rsa.pub**.

A chave pública tem que ser copiada para o seu servidor na internet, usando o comando

```

scp /root/.ssh/id_rsa.pub usuario@servidor.com:/home/usuario/
```

Agora faça login no servidor por ssh e adicione o arquivo da chave pública ao arquivos de chaves autorizadas a acessar o servidor por ssh:

```

cat id_rsa.pub >> /home/usuario/.ssh/authorized_keys
```

Faça logout e tente fazer login no servidor por ssh. Ele deve entrar diretamente, sem pedir a senha.

Ainda no servidor, edite o arquivo de configuração do daemon ssh

```

sudo pico /etc/ssh/sshd_config
```

Acrescente a linha **GatewayPorts yes**, salve o arquivo e reinicie o daemon com os comandos:

```

sudo systemctl restart sshd
```

Você pode testar a criação de um túnel executando esse comando no roteador:

```

ssh  -R 9000:localhost:22 usuario@servidor.com
```

Em seguida, faça login ssh no servidor em outro terminal e tente entrar no roteador com o comando:

```

ssh -p 9000 root@localhost
```

Ele vai pedir a senha do roteador e você deve cair no terminal dele.

Agora dê exit nas duas conexões acima para instalar o sshtunnel como serviço. Voltamos ao terminal do roteador e editamos o arquivo de configuração do sshtunnel:

```

vi /etc/config/sshtunnel
```

Use os dados do seu servidor no arquivo:

```

#esse é o servidor exposto na internet
# o nome de referencia essa é uma referencia interna do sshtunnel
config server nome_de_referencia
        option user                     usuario_no_servidor
        option hostname                 endereço_do_servidor
        option port                     22
        option retrydelay               5
        #arquivo de identidade no roteador
        option IdentityFile             /root/.ssh/id_rsa

#essa é a porta que vai ficar aberta no servidor
config tunnelR ssh
        #mesmo nome usado acima
        option server           nome_de_referencia
        option remoteaddress    *
        #essa é a porta usada para acessar o túnel. cada túnel tem que usar uma porta diferente
        option remoteport       9000
        option localaddress     127.0.0.1
        option localport        22
```

Faça o ssh tunnel rodar como serviço no momento do boot

```

/etc/init.d/sshtunnel enable
```

Reinicie o sshtunnel

```

/etc/init.d/sshtunnel stop
/etc/init.d/sshtunnel start
```

Agora você pode testar o túnel a partir do servidor com o mesmo comando anterior:

```

ssh -p 9000 root@localhost
```

O serviço sempre tenta manter o túnel aberto enquanto o roteador está ligado.

## Bônus: abrindo uma janela do seu browser na rede interna
Para navegar em um browser como se estivesse na rede local, você pode fazer assim:

Abra o túnel ssh a partir do roteador dentro da rede com um ip público:

```

ssh -R servidor:porta_no_servidor:localhost:22 usuario@servidor
```

Por exemplo:

```

ssh -R servidor.com:9000:localhost:22 eu@servidor.com
```

A porta no servidor não pode estar bloqueda pela firewall.

No seu PC, abra um túnel direto para o roteador com a opção -D:

```

 ssh -p porta_no_servidor usuario_no_roteador@servidor -Dporta_local
```

No exemplo anterior:

```

 ssh -p 9000 root@servidor.com -D8080
```

Agora abra outro terminal, e inicie o chromium através desta porta:

```

chromium-browser --proxy-server=socks://localhost:8080
```

Teste um endereço local da rede (do roteador, por exemplo), ou visite http://ipinfo.io. Você já não está na sua casa! (:
