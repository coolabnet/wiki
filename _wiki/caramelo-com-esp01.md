---
title: "Caramelo com ESP01"
layout: page
permalink: /caramelo-com-esp01/
---

**Lista de materiais**:
- O chip controlador com wifi, ESP-01.
  - https://lista.mercadolivre.com.br/esp-01
  - https://pt.aliexpress.com/wholesale?catId=0&SearchText=esp-01
- Um relé que vai ser acionado pelo chip e funciona como interruptor para o roteador. Tem que comprar um que já serve para o ESP-01. Na prática, sempre vendem o ESP01 e o relé juntos:
  - https://lista.mercadolivre.com.br/esp-01-relay
- O programador USB do ESP01
  - https://lista.mercadolivre.com.br/esp-01-programador
- **Atenção: muitas vezes vendem kits com esses três componentes.** Muito prático e por 60 reais tudo!
  - https://lista.mercadolivre.com.br/kit-esp-01-programador-rele

<figure><img src="{{ "/images/b/bc/Kit_esp-01.png" | relative_url }}" alt="KIt quase completo"><figcaption>KIt quase completo</figcaption></figure>
- Alimentação
  - Na placa do relé tem entrada para positivo e negativo. Ele aceita voltagens de 5 a 15V, e vai alimentar também o ESP-01.
    - Caso esteja usando alimentação por bateria de 12V, basta puxar um fio negativo/positivo para a placa.
    - Caso esteja usando eletricidade 110/220, você vai precisar de um adaptador 110/220 que dê entre 5 e 15V. Muitas vezes dá para usar um velhinho que não esteja sendo usado. É só desencapar os fios. Mas é importante ver qual o positivo e negativo. O melhor jeito é conferir com um multímetro. Não é garantido que a placa sobreviva se ligar na polaridade invertida.

**Programação**:
- O chip (o do teste, pelo menos) tinha um problema: para permitir a gravação dos programas, é necessário fazer um curto entre dois dos pinos do ESP-01. Como é muito difícil fazer um contato gambiarra estável, o melhor é soldar headers em todos os pinos. Ficou assim:

<figure><img src="{{ "/images/d/db/Programador_esp-01_com_headers.jpeg" | relative_url }}" alt="Programador com headers"><figcaption>Programador com headers</figcaption></figure>
- Use um jumper para conectar o pino 1 e 3, mais próximos ao plug USB. Assim:

<figure><img src="{{ "/images/e/e2/Programador_esp-01_com_jumper.jpeg" | relative_url }}" alt="Programador com jumper"><figcaption>Programador com jumper</figcaption></figure>
- Instale e rode o software para programação do chip, a plataforma Arduino:
  - https://arduino.cc/download/
- Baixe o programa principal daqui:
  - https://gitlab.com/coletivo-coolab/caramelo/-/archive/main/caramelo-main.zip
- Abra o arquivo caramelo.ino no programa acima
- Edite as linhas com o texto:
 #define MY_SSID "wifissid"
 #define MY_PSK  "wifipass"
Trocando wifissid e wifipass pelo nome da rede wifi e senha. Deixe só as aspas "" caso não tenha senha.
- Adicione a placa ESP8266 ao ambiente arduino (A ESP-01 é a própria ESP8266 com menos pinos e recursos).
  - Vá no menu File->Preferences
  - Adicione o texto "http://arduino.esp8266.com/stable/package_esp8266com_index.json" no "Additional boards manager URLs"
  - Agora entre em menu->tools->board->board manager. Procure por esp8266 e instale.
- Escolha a placa "Generic ESP8266 module"
- Escolha as seguintes configurações da placa:
  - Flash Mode: “DIO”
  - Flash Frequency: “40MHz”
  - CPU Frequency: “80 MHz”
  - Flash Size: “1M (64K SPIFFS)”
  - Debug Port: “Disabled”
  - Debug Level: “None”
  - Reset Method: “ck”
  - Upload Speed: “115200”
- Adicione a biblioteca de Ping ao programa:
  - Entre em Sketch->Include Libraries->Manage Libraries
  - Procure a biblioteca *ESP8266-Ping* e instale
- Conecte a plaquinha por USB no PC. Cada vez que se for programar, tem que desplugar e plugar de volta.
- Clique na seta -> para subir o programa para a plaquinha

**A parte elétrica**:
- Uma vez que o chip foi programado, já podemos colocar plugar no relé:
<figure><img src="{{ "/images/d/d0/ESP-01_com_relé.jpeg" | relative_url }}" alt="ESP-01 com relé"><figcaption>ESP-01 com relé</figcaption></figure>
- Para que o relé funcione como interruptor, o fio de alimentação elétrica do roteador tem que passar "por dentro" do relé. Então vamos cortar e desencapar um dos lados do fio, não importa se positivo ou negativo.
<figure><img src="{{ "/images/3/31/Cabo_de_alimentação.jpeg" | relative_url }}" alt="Cabo a ser cortado"><figcaption>Cabo a ser cortado</figcaption></figure>

<figure><img src="{{ "/images/4/47/Cabo_de_alimentação_aberto.jpeg" | relative_url }}" alt="Cabo com positivo e negativo separados"><figcaption>Cabo com positivo e negativo separados</figcaption></figure>

<figure><img src="{{ "/images/b/be/Cabo_de_alimentação_desencapado.jpeg" | relative_url }}" alt="Um dos lados desencapado"><figcaption>Um dos lados desencapado</figcaption></figure>

- Agora use os parafusos NC (normally closed) e COM (comum) para conectar os fios desencapados. Não importa qual vai em qual. As etiquetas estão na face de baixo da placa.
<figure><img src="{{ "/images/7/75/Relé_com_fios_do_roteador.jpeg" | relative_url }}" alt="Relé com fios do roteador e ESP-01"><figcaption>Relé com fios do roteador e ESP-01</figcaption></figure>

- Agora plugue os fios de alimentação, positivo no Vcc (direita na foto), negativo no GND (esquerda na foto).
<figure><img src="{{ "/images/0/0d/ESP-01_com_relé_e_fios.jpeg" | relative_url }}" alt="ESP-01, relé e conexões"><figcaption>ESP-01, relé e conexões</figcaption></figure>
- Pronto! Não esqueça de sempre testar antes de usar. E se o roteador estiver num lugar exposto, proteja o circuito dentro de um tupperware ou algo assim.
