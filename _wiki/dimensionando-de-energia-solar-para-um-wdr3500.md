---
title: "Dimensionando de energia solar para um wdr3500"
layout: page
permalink: /dimensionando-de-energia-solar-para-um-wdr3500/
---

A seguir vamos utilizar o modelo de dimensionamento de energia solar descrito em [Energia Solar Offgrid para roteadores em malha]({{ "/energia-solar-offgrid-para-roteadores-em-malha-2/" | relative_url }}) para um caso real, vamos calcular um sistema fotovoltaico relativo ao funcionamento de um [Wdr500](https://www.tp-link.com/us/home-networking/wifi-router/tl-wdr3500/#overview).

## Passo 1 - Calculando a potência de consumo diária
### Info de Entrada:
Olhando no manual de [especificações do equipamento](https://www.tp-link.com/us/home-networking/wifi-router/tl-wdr3500/#specifications)  obtemos os seguintes valores de entrada:

:\( V = 12v \)

:\( I = 1A \)

Calculando a Potência, com as seguinte regra:

:\(P_{total por dia} = P_{equipamento}\times{t}\)

temos:

:\(P_{equipamento} =12\times{1}=12W\)

Se o equipamento ficar ligado o dia todo temos:

:\(t=24h\)

### Dimensionamento:
Assim temos o seguinte consumo diário de energia:

\(P_{total por dia} =12\times{24}=288Wh &sdot; dia\)

## Passo 2 - Dimensionando a Bateria
Esse cálculo depende muito do tipo de bateria que estás usando. Aqui vamos considerar uma bateria estacionária de chumbo ácido, as mais comuns no mercado.

### Info de Entrada:
:Modelo de Descarga - `50% da bateria`

:Autonomia - `1 dia`

:Perda de `10%`

:\( V = 12v \)

:\(P_{total por dia} =288 W h &sdot; dia\)

### Dimensionamento:
Utilizando esse modelo temos a seguinte valor para a bateria

\(Capacidade\quad da\quad Bateria(Wh) =P_{totalpordia}\times{3}+0,1*P_{totalpordia}\)

Temos o seguinte:

\(Capacidade\quad da\quad Bateria(Wh) =288\times{3}+0,1*288\)

\(Capacidade\quad da\quad Bateria(Wh) = 892,8 Wh &sdot; dia\)

Porem os fabricantes informam esse valor em Ah, assim precisamos dividir pela tensão de trabalho, no nosso caso 12v.

\(Capacidade\quad da\quad Bateria(Ah) =\dfrac{892,8}{12}\)

Que resulta em:

\(Capacidade\quad da\quad Bateria(Ah) =74,4Ah &sdot; dia \)

O valor comercial mais próximo é de **80Ah**

## Passo 3 - Dimensionando o Painel Fotovoltaico
Nesse cálculo estamos considerando um Painel padrão.

### Info de Entrada:
Considerando uma realidade do sudeste do Brasil temos

:`Tempo de sol por dia: 5h`

:`Capacidade da bateria: 892Wh.dia`

### Dimensionamento:
- Potência em W do PV:

\(P_{painel} = \dfrac{Capacidade\quad da\quad Bateria}{t_{solpordia}}\)

\(P_{painel} = \dfrac{892,8Wh.dia}{5}\)

\(P_{painel} = 178,56 W\)

O valor comercial mais próximo é de **180 Wp**

## Passo 4 - Dimensionando o controlador de carga
### Info de Entrada:
As informações de entrada são duas já calculadas anteriormente

- Capacidade da Bateria (Ah)

- Tempo de sol por dia

### Dimensionamento:
Para saber a corrente de carregamento faça o seguinte:

\(I_{carregamento}=\dfrac{Capacidade\quad da\quad Bateria(Ah)}{t_{solpordia}}\)

\(I_{carregamento}=\dfrac{74,4Ah}{5}\)

\(I_{carregamento}=14,88 A\)

O valor comercial mais próximo é de **20A**

# Resultado final
Assim para um roteador *tl-wdr3500* nesse modelo adotado, vamos ter os seguinte componentes:

Bateria : **80 Ah**

Painel Fotovoltaico: **180 Wp**

Controlador de carga: **20A**
