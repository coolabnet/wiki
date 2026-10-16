---
title: "Aplicativos e serviços para redes locais"
layout: page
permalink: /aplicativos-e-servicos-para-redes-locais/
---

## Aplicativos para redes locais
#### TL;DR:
Qual o melhor aplicativo para chat e integração social em redes locais? Não existe um aplicativo ideal. Nossa conclusão é que temos que desenvolver um app que tire proveito das propriedades da rede LibreMesh. Em todo caso, aqui vão nossas escolhas:

- Aplicativo de chat p2p em rede libremesh: Kouchat -  https://f-droid.org/en/packages/net.usikkert.kouchat.android/. Desvantagem: tem muito poucos recursos
- Aplicativo de chat p2p em redes domésticas: WiFi Talkie - https://apkpure.com/talkie-wi-fi-calling-chats-file-sharing/com.remaller.android.wifitalkie_lite/download?from=details
- Melhor aplicativo de rede social p2p: Manyverse. Mas só para celulares com bastante memória e processamento.
- Melhor plataforma de serviços locais: Yunohost

### Relatório completo
A CooLab pesquisou aplicativos de celular que possam ser úteis para usuários redes redes locais e que possam contribuir com a integração da comunidade. Para isso, escolhemos alguns critérios:

- O aplicativo tem que ter versão para Android, que é praticamente o único sistema utilizado por usuárias em nossas redes
- O aplicativo tem que ocupar muito pouco espaço, uma vez que uma das barreiras para adoção de um aplicativo é não ter espaço no dispositivo para instalacão
- Tem que funcionar sem problemas em redes LibreMesh, onde os testes foram feitos.
- Preferencialmente tem que funcionar mesmo sem conexão com a internet (somente com os pares locais)
- Preferencialmente tem que poder ser instalado mesmo sem conexão com a internet (através de apk ou f-droid e sem necessidade de registro em servidor central)
- Preferencialmente tem que ter funcionalidade P2P, ou seja, sem necessidade de um servidor central com auto-descoberta de pares. No caso que um servidor seja necessário, ele deverá estar localizado na rede local.
- Preferencialmente com versão em português

Apesar de apontar algumas plataformas de rede social, conteúdo local e notícias, na primeira parte vamos nos focar em aplicativos de chat. Segue a lista dos programas testados e suas avaliações.

#### Apps
##### Chats
- **Lan Messenger**
    - https://play.google.com/store/apps/details?id=com.nabinbhandari.lam.android
    - https://apkpure.com/lan-messenger-p2p-offline-chat-and-file-sharing/com.nabinbhandari.lam.android
    Instalou sem Internet. Não esta no F-Droid.
    Tamanho de apk/instalado/uso de memória: 1.4Mb/1.4Mb/56Mb
    Rede doméstica: funcionou rápido, encontrou pares, faz chat e tramsferência de arquivos
    LibreMesh: demorou muito para achar pares, mensagens demoraram muito. Impraticável.

- **Softros lan messenger**
    - https://play.google.com/store/apps/details?id=com.Softros.softros_lan_messenger
    - https://apkpure.com/softros-lan-messenger/com.Softros.softros_lan_messenger
    Instalou sem Internet. Não esta no F-Droid.
    Tamanho de apk/instalado/uso de memória: 4.3Mb/7.3Mb/73Mb
    Rede doméstica: Chat muito lento. Algumas mensagens nunca foram entregues.
    LibreMesh: Não funcionou.

- **Wifi Talkie**
    - https://play.google.com/store/apps/details?id=com.remaller.android.wifitalkie_lite
    - https://apkpure.com/talkie-wi-fi-calling-chats-file-sharing/com.remaller.android.wifitalkie_lite/download?from=details
    Instalou sem Internet. Não esta no F-Droid.
    Tamanho de apk/instalado/uso de memória: 6.7Mb/16Mb/127Mb
    Rede doméstica: Muito rápido, permite chamadas de voz.
    LibreMesh: Não funcionou.
    Obs. Permite usar o próprio aparelho celular como roteador

- **Kouchat**
    -  https://f-droid.org/en/packages/net.usikkert.kouchat.android/
    Instalou sem internet
    Tamanho de apk/instalado/uso de memória: 2.5Mb/3.4Mb/68Mb
    Rede doméstica: Achou pares e trocou mensagens muito rápido
    LibreMesh: Demorou para achar pares, mas uma vez que achou, as mensagens vieram rápido
    Obs. Muito simples. Só oferece uma sala de chat geral.

- **Jami**
    - https://f-droid.org/en/packages/cx.ring/
    Exige cadastro em servidor central. Portanto não permite instalação sem internet.
    Possibilidade de instalar servidor local. https://jami.net/services/
    Tamanho de apk/instalado: 33Mb/66Mb

- **Meshenger**
    - https://github.com/meshenger-app/meshenger-android
    Quando a conversa acontece em um node funciona bem mas quando testado na rede, as pessoas encontraram dificuldade, porque o aplicativo não encontrava as pessoas

- **Serval**
    - http://www.servalproject.org/
    Testado e usado para chamadas. Serval tem seu proprio sistema de roteamento atraves do Serval Mesh

- **Briar**
    - https://briarproject.org/how-it-works/
    Problema logo no começo, quando cadastra as pessoas com QR code

##### Redes sociais
- **Retroshare**
    - https://f-droid.org/en/packages/org.retroshare.android.qml_app/
    Instalou sem internet.
    Tamanho de apk/instalado/uso de memória: 14Mb/53Mb/138Mb
    Rede doméstica/libremesh: Não passou da tela de criar profile

- **Manyverse**
    - https://f-droid.org/en/packages/se.manyver/
    Instalou sem internet.
    Tamanho de apk/instalado/uso de memória: 33Mb/93Mb/199Mb
    Rede doméstica/libremesh: funcionou bem, achou pares.
    Mas requer muita memória e processamento (constantemente fazendo updates)

#### Servidor Local
Em seguida, relacionamos os aplicativos que exigem a instalação de um servidor local. O servidor de testes foi uma raspi 3 modelo B. Testamos duas plataformas de servidores locais que serão descritas a seguir.

##### Chat
- **Nextcloud Chat**
    - Requer configurar com o endereço do servidor local. Exige criar conta antes no servidor, o que é uma limitação.
    - Funcionou bem com o Ubos.

- **Mattermost**
    - Não pudemos testar em servidor local

##### Rede social
- **Mastodon (fediverse)**
    - Ubos via nextcloud - não funcionou. O cliente de android não conectou com o servidor local.
    - Yunohost. Não funcionou por questões de domínio.

##### Plataformas de serviços locais
- **Ubos**
     - http://ubos.net/
     - Instalado por cartão SD na raspi. Necessita conhecimento de ssh por terminal para configuração. Para login é necessário criar um pendrive com nome UBOS-STAFF e gravar nele a chave pública ssh. Aplicaççoes instaladas: nextcloud com nextcloud-spreed (chat), nextcloud-bookmarks, nextcloud-audioplayer, nextcloud-social (fediverse), nextcloud-notes. Mastodon e Mattermost ainda estão em beta e não puderam ser instaladas.

- **Yunohost**
     - https://yunohost.org/
     - Exige uma conexão por cabo de rede (ou fazer a instalação via terminal). A inteface é muito amigável. Mas no momento, quase todos os aplicativos só rodam em PC (não funcionam na Raspi)

##### Plataformas de conteúdos locais com foco em educação
- **Rachel**
    - http://rachelfriends.org/rachel-pi-howto.html
    - Rachel oferece um arquivo de 64Gb e necessita de um cartão de memória com essa capacidade. Portanto não pode ser testado. Além disso, os idiomas oferecidos são inglês, espanhol e francês, portanto estaria fora de nossos critérios

- **Internet in a box**
    - http://internet-in-a-box.org/
    - Além de diversos aplicativos como o nextcloud e wordpress, o IIAB oferece diversos conteúdos educacionais através do Kolibri e Sugarizer. Ele rodou bem instalado na Raspberry PI. Como pontos negativos, ele oferece pouco conteúdo em português; e os conteúdos demoram muito a baixar e instalar, mesmo com uma internet rápida. A instalação consiste em primeiro configurar uma Raspbery Pi com sistema Raspbian, e em seguida usar o terminal para instação do conteúdo e configuração. O design não é atraente.

Extra: a melhor lista de aplicações self-hosted - https://github.com/awesome-selfhosted/
