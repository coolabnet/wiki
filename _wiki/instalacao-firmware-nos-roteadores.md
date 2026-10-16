---
title: "Instalação firmware nos roteadores"
layout: page
permalink: /instalacao-firmware-nos-roteadores/
---

Para fazermos uma rede mesh, primeiro devemos pensar e desenhar essa rede. Com equipamentos necessários em mãos, vamos começar substituindo os firmwares (espécie de sistemas que rodam dentro dos roteadores) proprietários e com limitações para a criação da rede mesh. Vamos substituir por um sistema baseado em openwrt que é um sistema livre que nos permitirá a criação da rede mesh utilizando roteadores comuns.

Podemos baixar o firmware em:

chef.altermundi.net

- Tem que tentar vários sistemas as vezes até instalar um firmware que vai funcionar legal.

Esse firmware é baseado em **openwrt**, uma vez no altermundi, vamos colocar as características (fabricante, modelo, etc) do nosso equipamento e da rede que estamos criando. Se nessa rede estivermos usando mais de um modelo de equipamento, vamos descrever todos lá e vai baixar um arquivo para cada tipo de equipamento.

A maioria dos roteadores que instalando aqui não está no mercado. Os fabricantes foram mudando o firmware agora vem numa versão já atualizada que não permite a substituição do firmware de fábrica. Então tem que achar na internet o antigo firmware dele mesmo para instalar uma versão de firmware mais antiga (podemos chamar de downgrade?) permitindo assim a instalação de um firmware diferente no caso nosso firmware baseado em openWRT ou seja um firmware livre.

Isso vai melhorar com o LibreRouter! Que será um roteador livre ou seja um hardware livre que não terá uma limitação de uso em seu software.

**Importante**: Quando forem comprar roteador pesquisar por modelos que rodem openwrt e libremesh. O Ideal seria podermos usar qualquer um, mas muitos roteadores não tem memória suficiente (tipo o 740 e o 741), você consegue por só um pequeno pacote. (que você precisa vem marcado como mini ou 0.  - anotei isso mas não entendi, alguém pode melhorar essa explicação?)

Vamos fazer um cadastro no chef e ver como funciona:

chef.altermundi.org

Como conectamos esses roteadores?

Se você quiser conectar a escola até a praça que fica a 3km, então precisamos de um roteador direcional (vai para frente o sinal, para onde apontarmos), e tem a opção de link a distância, tem potência mais alta que outros, e só quem tiver mais longe conecta nele. Para planejar a rede tem que saber qual equipamento ideal para usar em cada situação.

Vamos substituir o firmware de um roteador da TP-LINK que está com o firmware instalado de fábrica.

Estamos usando: modelo: CPE210 da TP-LINK – Pharos.

O Roteador vai ser conectado na energia elétrica via cabo de rede. Prestar atenção para não queimar. Voltagem 24V – 1A. Vai conectado o **cabo de rede** **na porta: LAN0 (POE IN)**

## Documentação da instalação do openWRT no roteador TP-LINK - modelo: CPE210
**A documentação abaixo foi toda feita utilizando Debian Stretch.

Vai no chef.altermundi e coloca o modelo do aparelho. Se você já tiver informação da rede que vai ser feita, você já pode colocar. Mas se não colocar ele vem com um padrão para você alterar posteriormente.

O **altermundi** é uma interface entre os desenvolvedores e as comunidades.

**Openwrt** – te permite instalar o **libremesh** mas o foco do projeto é ser um **sistema livre para roteador**. Distribuição livre para roteador.

**Libremesh** – é para fazer uma rede **automagicamente** usando o openwrt**.

---
Uma vez em:

https://chef.libremesh.org/

Preenchemos:

**Distribution**: Libremesh

**Router Model**: CPE210
**
Network Profile**:

---
Como o chef não estava funcionando entramos no:

**Github** – onde um dos projetos hospedados é o libremesh.

; github
: Definfição: é um local onde as pessoas armazenam e distribuem códigos fontes de projetos.

- O chef altermundi é uma ferramenta de construção de firmware livre para roteadores, ele é alimentado pelo github.

Entramos no repositório:

https://github.com/libremesh

Para quem quiser mexer no **SDK**:

Vai **target** –> profile → **flavour**

Qual o **chipset** do equipamento. O libremesh fala para você. Precisa saber o tipo de processador para criar o firmware.

O **flavour** é completa, mini ou com ambiente gráfico ou só linha de comando. No nosso caso colocamos completa.

O **SDK** é tudo explicadinho passo a passo. Para **cozinhar** na própria máquina. (por favor definiam cozinhar)

- O objetivo é substituir o sistema operacional do equipamento, pode-se fazer de várias formas, as vezes está pronto e é fácil e quando não tá pronto é que se faz o processo aí de cima.

Apareceram várias opções para download no chef.libremesh:

 Created files
 build-253f9528397d7e3.log
 lime-17.06-a0f0a07990d3c9e-ar71xx-generic-cpe210-220-squashfs-factory.bin
 lime-17.06-a0f0a07990d3c9e-ar71xx-generic-cpe210-220-squashfs-sysupgrade.bin
 lime-17.06-a0f0a07990d3c9e-ar71xx-generic-device-cpe210-220.manifest
 lime-17.06-a0f0a07990d3c9e-ar71xx-generic-root.squashfs
 lime-17.06-a0f0a07990d3c9e-ar71xx-generic-uImage-lzma.bin
 lime-17.06-a0f0a07990d3c9e-ar71xx-generic-vmlinux-lzma.elf
 lime-17.06-a0f0a07990d3c9e-ar71xx-generic-vmlinux.bin
 lime-17.06-a0f0a07990d3c9e-ar71xx-generic-vmlinux.elf
 lime-17.06-a0f0a07990d3c9e-ar71xx-generic-vmlinux.lzma
 sha256sums
 sha256sums.sig

Provavelmente vamos usar um arquivo **.bin** para substituir o firmware de nosso roteador.

A diferença das primeiras duas opções de download .bin são:

;Factory
: Se o roteador esta com o firmware de fábrica se usa o factory.

;Sysupgrade
: Se você já mexeu no firmware no do seu roteador e vai só atualizar você usa o sysupgrade.

Fizemos o download do **factory**, já que nosso roteador estava com firmware original. O factory abre as portas para poder fazer a substituição do firmare proprietário para o firmware livre baseado em openWRT, compilado especificamente para a marca e modelo de seu roteador para assim ser possível fazermos a rede mesh.

Depois disso temos que verificar o download! Muito importante por pelo menos 2 motivos:

- garantir que o arquivo que baixou foi baixado com integridade.

- para confirmar origem do arquivo! Sua autenticidade.

Como ele está com o firmware original baixamos as 2 versões tanto a factory quanto a sysupgrade (essa informação conflita com a de 4 parágrafos acima, alguém pode revisar?)

Agora conectamos fisicamente o computador ao roteador. Colocamos um cabo de rede no POE para alimentar ele com energia! Como tinhamos uma fonte ligamos no POE da fonte e no POE do roteador, e ligamos com outro cabo de rede na porta LAN do computador para o roteador também na porta LAN. Por alguma magia do universo para completar a configuração dos roteadores em alguns momentos precisamos desconectar esses cabos e mudar de porta. (isso é estranho se alguém conseguir dar uma informação mais precisa sobre isso!)

Pega no manual do roteador como faz para conectar conectar nele através do seu computador uma vez que tem um cabo de rede conectado entre seu computador e o roteador, para assim poder fazer a configuração.

Para conectarmos com o roteador, mexemos na conexão de rede do debian:

Fomos editar conexões -> na configuração de rede seleciona - conexão por cabo→ troca método para manual → em configurações IPV4
no endereço colocar: **192.168.0.10**

Na mascara de rede pode ser: **24**

 Para fazer no windows vamos em ethernet → status → propriedades → vai em protocolo IP versão (TCP/IPV4) → muda para manual → **192.168.0.10**
 depois
 **255.255.255.0**
 Ok. Vai no navegador e digita:
 **192.168.0.254**
 Continua da mesma forma que no Debian.

---
Antes de entrar no roteador para instalar o novo firmware, conferimos o arquivo que baixamos com o hash dele, que estava disponível no chef! Com isso conferimos se o arquivo é exatamente igual ao arquivo baixado!

Vamos entrar no roteador agora:

Ver no manual do seu roteador, neste caso, vamos no navegador e digitamos:

**192.168.0.254**

Agora temos acesso a configuração do roteador :

Vamos em **System** -> Em firmware, vamos dar upload do arquivo factory baixado.

As vezes por alguma razão mágica não conseguimos fazer o upload do arquivo. Uma boa tentativa é renomear o arquivo para um nome com menos caracteres e tentar novamente. No caso só funcionou após mudar o nome para 1.bin

Depois de subir o firmware você acessa novamente pelo navegador:

**http://thisnode.info**

---
Vamos estabelecer o **nome do sistema**:

Tem uma questão importante que é: O libre mesh associa ao nome da rede SSID com o prefixo do seu IP. Não tem uma forma fácil de resolver.

Tem que entrar no roteador a partir da linha de comando para poder fazer isso, pois se fizer isso pelo navegador não vai funcionar pois não vai mudar o endereço IP da rede. Dá certo, mas pode dar problema para conectar com um servidor local, para trocar arquivos e etc…

Para conectar via linha de comando, abra um terminal e digite:

 ssh root@thisnode.info

Modificamos dois parametros no arquivo lime-defaults, digitando no terminal:

 vi /etc/config/lime-defaults

E modificamos o nome da rede nesses dois parâmetros:

 option ap_ssid 'NomeDaSuaRede'

 option apname_ssid 'NomeDaSuaRede/%H'

---
Temos a possibilidade de cozinhar o nome da rede com o o **cooker** já com o nome da comunidade. Ou mudar o artigo de configuração no lime.config – para fazer em todos.

Com o cooker você consegue fazer um arquivo que vai instalar as informações da sua rede comunitária para todos os computadores.

(não consegui fazer a documentação dessa parte, se alguém tiver a manha, manda aê)

## Glossário:
;openWRT
: Definição:

;LibreMesh
: Definição:

;firmware
: Definição:

;LibreRouter
: Definição:

;roteador direcional
: Definição:

;link longa distância
: Definição:

;porta LAN
: Definição:

;cabo de rede
: Definição:

; github
: Definfição: é um local onde as pessoas armazenam e distribuem códigos fontes de projetos.

;SDK
: Definição:

;chipset
: Definição:

;debian
: Definição:

;hash
: Definição:

;rede SSID
; Definição:

;IP
; Definição:
