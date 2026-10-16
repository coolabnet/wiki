---
title: "Caramelo com ESP8266"
layout: page
permalink: /caramelo-com-esp8266/
---

**Lista de materiais**:
- O chip controlador com wifi. Usamos um chip baseado em ESP8266, mas outros chips com wifi como o ESP32 serviriam. Você pode comprar de marca, como Adafruit, ou uma versão chinesa como NodeMCU. Aqui vão alguns links para busca e compra:
  - https://lista.mercadolivre.com.br/esp8266
  - https://pt.aliexpress.com/wholesale?catId=0&SearchText=esp8266
  - Custo: 40-50 reais.
- Um relé que vai ser acionado pelo chip e funciona como interruptor para o roteador. O melhor é comprar um que já vem completo com o circuito para ser controlado. Existem pelo menos dois tipos:
  - Simples, que só tem um circuito de proteção contra descargas elétricas (diodo). Como esse:https://gitlab.com/coletivo-coolab/caramelo
    - https://produto.mercadolivre.com.br/MLB-1475000180-rele-1-canal-5v-modulo-arduino-esp8266-nodemcu-esp32-rpi-_JM#position=12&type=item&tracking_id=3ffa4add-fb97-4b2b-aaaa-9548b98b0e9c
  - Com chip, que se comunica com o controlador através de um protocolo chamado i2c. Como esse (que é o que usamos de teste):
    - https://www.sparkfun.com/products/15093
  - Custo: 15-30 reais
- Cabo USB Micro B para programar o chip
- Alimentação do chip e relé.
  - Caso o roteador seja alimentado por bateria 12V, você precisa de um transformador do tipo de carros, de 12V para 5V. https://lista.mercadolivre.com.br/carregador-celular-12v
  - Caso esteja ligado em 110/220v, vai precisar de um carregador USB normal.
- Normalmente o chip e o relé vem sem conexões e você precisa soldar um ao outro. Você pode optar por soldar diretamente na placa, ou soldar um "header" e usar "jumper cables". Veja as fotos para entender a diferença. Não recomendamos soldar na placa, já que vai ser difícil desfazer caso necessário, e há mais risco de soldar errado. De um jeito ou de outro, vai precisar de um ferro de soldar e estanho
  - https://lista.mercadolivre.com.br/barra-de-pinos-macho-arduino
  - https://lista.mercadolivre.com.br/cabos-jumper-femea

Essa é a placa ESP8266 usada. Vamos primeiro conectar ela por USB no PC e programá-la.

<figure><img src="{{ "/images/5/58/ESP8266_FEATHER_HUZZAh.jpeg" | relative_url }}" alt="PLaca ESP8266, versão Feather Huzzah da Adafruit"><figcaption>PLaca ESP8266, versão Feather Huzzah da Adafruit</figcaption></figure>

**Programação**:
- Instale e rode o software para programação do chip, a plataforma Arduino:
  - https://arduino.cc/download/
- Baixe o programa principal daqui:
  - https://gitlab.com/coletivo-coolab/caramelo/-/archive/main/caramelo-main.zip
- Abra o arquivo caramelo.ino no programa acima
- Edite as linhas com o texto:
 #define MY_SSID "wifissid"
 #define MY_PSK  "wifipass"
Trocando wifissid e wifipass pelo nome da rede wifi e senha. Deixe só as aspas "" caso não tenha senha.
- Apague as duas barras do começo da linha que diz
 //#define USING_I2C 1
Deixando assim:
 #define USING_I2C 1
- É possível que seja necessário instalar esses drivers no computador, para que a placa ESP8266 seja reconhecida (no linux não precisa, só mac e windows):
  - http://www.silabs.com/products/development-tools/software/usb-to-uart-bridge-vcp-drivers
- Adicione a placa ESP8266 ao ambiente arduino.
  - Vá no menu File->Preferences
  - Adicione o texto "http://arduino.esp8266.com/stable/package_esp8266com_index.json" no "Additional boards manager URLs"
  - Agora entre em menu->tools->board->board manager. Procure por esp8266 e instale.
- Adicione a biblioteca de Ping ao programa:
  - Entre em Sketch->Include Libraries->Manage Libraries
  - Procure a biblioteca *ESP8266-Ping* e instale
- Se o relé tiver chip, adicione a biblioteca qwiic relay à plataforma arduino:
  - Entre em Sketch->Include Libraries->Manage Libraries
  - Procure a biblioteca qwiic relay e instale a biblioteca *sparkfun qwiic relay*
- Conecte a plaquinha por USB no PC
- Selecione a placa ESP8266 no menu board
- Clique na seta para subir o programa para a plaquinha

**A parte elétrica**:
- Solde os pinos no chip e relé conforme as fotos. Vamos soldar 4 headers nos buracos RST, 3V, NC, GND (de onde vamos tirar os 3V para alimentar o relé) e mais 4 nos buracos SDA, SDL, 2, 16, de onde sai a comunicação via i2c.
<figure><img src="{{ "/images/a/a5/ESP8266_e_headers.jpg" | relative_url }}" alt="ESP8266 e os headers"><figcaption>ESP8266 e os headers</figcaption></figure>

No relé, vamos soldar 4 headers - GND, 3.3V, SDA, SCL.

<figure><img src="{{ "/images/6/63/Relay_sem_headers.jpg" | relative_url }}" alt="O relé e os headers"><figcaption>O relé e os headers</figcaption></figure>

- Agora é só usar 4 fios jumper fêmea-fêmea para conectar os headers GND, 3V, SDA e SCL.
<figure><img src="{{ "/images/f/f0/ESP8266_e_RELÉ.jpeg" | relative_url }}" alt="O ESP8266 e o relé conectados pelos 4 fios"><figcaption>O ESP8266 e o relé conectados pelos 4 fios</figcaption></figure>

- Para que o relé funcione como interruptor, o fio de alimentação elétrica do roteador tem que passar "por dentro" do relé. Então vamos cortar e desencapar um dos lados do fio, não importa se positivo ou negativo.
<figure><img src="{{ "/images/3/31/Cabo_de_alimentação.jpeg" | relative_url }}" alt="Cabo a ser cortado"><figcaption>Cabo a ser cortado</figcaption></figure>

<figure><img src="{{ "/images/4/47/Cabo_de_alimentação_aberto.jpeg" | relative_url }}" alt="Cabo com positivo e negativo separados"><figcaption>Cabo com positivo e negativo separados</figcaption></figure>

<figure><img src="{{ "/images/b/be/Cabo_de_alimentação_desencapado.jpeg" | relative_url }}" alt="Um dos lados desencapado"><figcaption>Um dos lados desencapado</figcaption></figure>

Agora use os parafusos NC (normally closed) e COM (comum) para conectar os fios desencapados. Não importa qual vai em qual.

<figure><img src="{{ "/images/5/52/Relé_conectado.jpeg" | relative_url }}" alt="Relé conectado aos fios de alimentação do roteador"><figcaption>Relé conectado aos fios de alimentação do roteador</figcaption></figure>
