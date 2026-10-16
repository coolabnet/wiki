---
title: "Energia Solar Offgrid para roteadores em malha"
layout: page
permalink: /energia-solar-offgrid-para-roteadores-em-malha-2/
---

# Intro
Em alguns casos quando precisamos adicionar um novo ponto na rede mesh e não temos energia elétrica disponível, precisamos montar um sistema autônomo de energia.
Existem algumas alternativas atualmente, mas vamos focar em especial na energia solar fotovoltaica (não confundir energia solar térmica, para aquecimento de água).
O sistema funciona com um painel com um material fotovoltaico, isso significa que é um material que capta a irradiação solar e transforma em energia elétrica. Mais profundamente podemos dizer que essa placa contém um material que cria uma diferença de potencial (ou tensão *U*, popularmente conhecido como 'voltagem') dada em Volts (com simbolo *V*)

## Componentes
Precisamos entender cada componente do sistema para dimensionar adequadamente e não haver perdas energéticas e nem financeiras. Vamos dividir os componentes em:

- Carga - no nosso caso um roteador
- Painel Fotovoltaico - para captar a radiação solar e converter em energia elétrica
- Bateria - para armazenar a energia do sol
- Controlador de carga - proteger a bateria

Existem muitas maneiras de calcular os componentes de um sistema fotovoltaico, aqui vamos mostra um modelo básico de dimensionamento.

# Modelo de Dimensionamento
Um modelo de dimensionamento significa aplicar as leis da física para o consumo energético de acordo com algumas escolhas que vamos fazer para cada componente. Isso vai depender muito da localidade que vai ser instalado o sistema (cada localidade tem uma quantidade de sol diferente e consequentemente uma quantidade de energia disponível distinta) ou o quanto temos para gastar com isso.

Para ficar mais fácil e não confundir todas as contas, vamos dividir as informações de cada componente em dois tipos:

- **Informação de Entrada** - Valores iniciais necessários para fazer o dimensionamento do componente.

- **Dimensionamento** - Resultado do cálculo para o componente, esse valor vai ser a informação que vamos procurar na hora de comprar.

O fluxograma abaixo mostra com mais detalhes a sequência do modelo que vamos adotar:

<figure><img src="{{ "/images/3/30/Dimensionamento-solar.png" | relative_url }}" alt="Fluxograma do cálculo das características dos componentes"><figcaption>Fluxograma do cálculo das características dos componentes</figcaption></figure>

## Carga
A Carga de um roteador varia muito de acordo com o uso dele, se tem mais clientes conectados ou se esses clientes estão conectados o tempo todo vai consumir mais energia, se não está sendo usado muito vai consumir menos. O ideal é calcular pelo valor máximo da energia consumida.

### Info de Entrada:
- Potência do equipamento

A potência do equipamento é uma informação que deve constar na etiqueta do produto (exemplo [https://www.tp-link.com/resources/UploadFiles/Images/20150204111603.png](https://www.tp-link.com/resources/UploadFiles/Images/20150204111603.png)), normalmente seguido da palavra *OUTPUT* ou *POWER*. Um número seguido da letra 'W' ou da palavra 'Watts'[1]. Se não constar essa informação no equipamento procure por números seguidos das letras 'V' (tensão) e 'A' (corrente elétrica) e multiplicando esses dois números você encontra a Potência('W').

- Tempo Ligado

O tempo que cada equipamento a dada potência vai ficar ligado, em horas.

### Dimensionamento:
- Potência total por dia

Para calcular a potência total em um dia é só multiplicar a Potência de cada equipamento pelo tempo, em horas, que ele vai ficar ligado. No nosso caso se é só um equipamento fazemos:

::::::::<table><tbody><tr><td></td></tr></tbody></table>

## Bateria
A Bateria é o mal necessário do nosso sistema, é o item mais caro por durar menos tempo. E se dimensionado errado o sistema, a bateria pode durar apenas 1 ano, e na melhor das hipóteses, uma bateria de chumbo ácido vai durar 5 anos. Outras baterias duram mais e poluem menos, porém são mais caras.

> **Nota:** Baterias de chumbo ácido são muito poluentes e devem ser descartadas em locais apropriados, consulte o fabricante!

### Info de Entrada:
- Tensão de Trabalho

A tensão em que o sistema vai trabalhar, ou seja, a tensão necessária para ligar o equipamento. Na maioria das vezes vamos usar 12V ou 24. Como cada bateria normalmente tem 12v se quisermos usar em 24v precisamos de duas baterias em paralelo, assim como fazemos com as pilhas no controle remoto.
Alguma vezes se for ligar equipamentos em voltagem distintas pode se usar um conversor de tensão

- Modelo de Descarga

O modelo de descarga via depender do tipo de bateria que se deseja utilizar. Se for uma bateria estacionaria de chumbo ácido (as mais comuns para sistemas fotovoltaicos) utiliza-se o seguinte modelo

1- *descarga de 50%*: Para aumentar o tempo de vida útil das baterias é aconselhável que não se descarregue a menos da metade dela, ou seja que a capacidade dela seja o dobro da quantidade de energia que vamos precisar por dia.

2- *perda de 10%*: Assumimos uma perda de 10% devido a fatores não controláveis, mas esse valor pode variar.

- Autonomia

Esse dado é uma escolha de segurança, um valor normalmente utilizado é 5 dias de autonomia, ou seja, devemos somar cinco vezes a mais o valor da energia do(s) equipamento(s).

### Dimensionamento:
- Capacidade da Bateria

Assim temos que somar:

1- *descarga de 50%*:\( = E_{totalpordia} \)

2- *perda de 10%*:\( = 0,1\times{E_{totalpordia}}\)

3- *5 dias de autonomia*: \( = 5\times{E_{totalpordia}}\)

Somando tudo temos:

:\(Capacidade\quad da\quad Bateria = E_{totalpordia} + E_{totalpordia} +5\times{E_{totalpordia}} + 0,1\times{E_{totalpordia}}\)

ou

:\(Capacidade\quad da\quad Bateria = 7,1\times{E_{totalpordia}}\)

Como as baterias no mercado são descritas pela capacidade em Ah, e esse valor é dado em 'W', devemos dividir esse valor pela tensão de trabalho da bateria no sistema:

::::::::<table><tbody><tr><td></td></tr></tbody></table>

É importante analisar qual a corrente de carregamento para essa bateria, pois se a corrente for muito alta vai ser necessário fios mais grossos para suportar e cobre é caro.
Então por mais que o(s) equipamento(s) trabalhe(m) em 12v as vezes é mais barato montar um sistema em 24v e usar o conversor de tensão para regular a tensão apropriada.
Logo abaixo, secção do controlador de carga vamos calcular essa corrente.

## Painel Fotovoltaico
Para saber a energia necessária que o painel fotovoltaico precisa produzir vamos considerar que ele seja capaz de carregar toda a bateria durante o período de sol diário.

### Info de Entrada:
- *Tempo de sol diário*: A quantidade de sol que tem no local da instalação. Esse valor vai depender da irradiação solar na sua região do globo terrestre, [no Brasil temos Atlas Brasileiro de Energia Solar](http://urlib.net/rep/8JMKD3MGP3W34P/3PERDJE) que fornece o tempo de sol em cada canto do país. Mais ainda assim é preciso considerar o microclima do local. Tem locais de montanhas que passam muito tempo nublado devem ser considerados no cálculo

- *Perda*: Nunca conseguimos extrair toda energia que o painel produz, normalmente um controlador de carga mppt perde ao menos 30% de energia.

- *Energia total por dia*: vamos dimensionar o sistema em cima da energia total por dia que é consumida

### Dimensionamento:
Devemos somar a energia consumida por dia a perda, equivalente a 30%:

- *Perda*: \( = 0,3\times{E_{totalpordia}}\)

Assim calculamos a potencia do painel considerando a energia com a perda:

\(E_{painel+perda} = E_{totalpordia} + 0,3\times{E_{totalpordia}}\)

- Potência em W do PV:

\(E_{painel} = \dfrac{E_{painel+perda}}{t_{solpordia}}\)

Esse valor deve ser avaliado pois dificilmente o resultado vai ser um valor de potencia de um painel comercial. Essa analise deve constar os seguistes critérios:

- se o valor der muito próximo podemos arredondar para cima ou para baixo, mas tome cuidado não diminua o valor mais do que a 10% da carga diária de consumo do equipamento.

- é sempre mais barato comprar um único painel fotovoltaico do que dois de uma potência menor para associar e chegar na potencia desejada, e essa escolha ainda vai acarretar em custo adicional com conectores mc4 que são caros.

> **Nota:** Ao associar painéis fotovoltaicos tome sempre cuidado com três coisas:
- use sempre painéis exatamente iguais, em características elétricas (Tensão e Corrente) e de fabricação
- associação em paralelo dobra a corrente!. Confira no controlador de carga se essa corrente não excede seu limite
- a tensão de máxima potência (*Vmp*) dos painéis tem que ser pelo menos 50% maior que tensão total das baterias

## Controlador de Carga
Para dimensionar o controlador de carga precisamos saber qual o valor da maior corrente elétrica no sistema. Essa corrente é a corrente de carregamento da bateria pois é onde o sistema vai trocar mais energia em menos tempo.

### Info de Entrada:
As informações de entrada são duas já calculadas anteriormente

- Capacidade da Bateria (Ah)

- Tempo de sol por dia

### Dimensionamento:
Para saber a corrente de carregamento faça o seguinte:

\(I_{carregamento}=\dfrac{Capacidade\quad da\quad Bateria(Ah)}{t_{solpordia}}\)

Novamente devemos analisar esse valor para descobrir qual controlador comprar, normalmente eles são de 10A, 20A e 30A, devemos sempre arredondar para cima pois um pico de corrente acima desse valor pode ser fatal.

> **Nota:** O controlador de carga vai rebaixar a tensão dos painéis para adequar ao banco de baterias. No controlador PWM, esse rebaixamento de tensão se configura uma perda de potência do sistema. No MPPT, ele aumenta a corrente para compensar, mantendo o ponto de máxima potência dos painéis solares. Assim para saber se o seu controlador de carga é MPPT vc precisa medir a corrente de saída, ela  deve ser maior do que a de entrada.

# Apêndice
## A diferença entre Volts (V) e Watts (W)
### Tensão - volts
Volts  é a unidade de medida de tensão, quando a gente fala que a bateria tem 12V estamos nos referindo tensão elétrica, ou a diferença de potencial entre os dois terminais da bateria.

A tensão(U) em um circuito é dada pela:

::::::::<table><tbody><tr><td></td></tr></tbody></table>

Onde:

*R* - Resistência, dado em ohms (&Omega;)

*U* - Diferença de Potencial dado em volts (*V*)

*I* - Corrente elétrica dado em amperes (*A*)

### Potência - Watts
Já Watts é a unidade de potência ou a energia total em um determinado tempo, normalmente relacionado ao consumo dos equipamentos
A Potência Elétrica em um circuito é dada pela equação:

::::::::<table><tbody><tr><td></td></tr></tbody></table>

Onde:

*P* - Potencia elétrica, dada em (*W*)

*U* - Diferença de Potencial dado em volts (*V*)

*I* - Corrente elétrica dado em amperes (*A*)

> **Nota:** Normalmente a informação da potência nos equipamentos, dada em Watts(*W*) significa a potência consumida durante 1h de uso.

Algumas informações matemáticas para facilitar o entendimento:

- Abreviações de potências:

:Sempre que ver algo como *kW* imagine o seguinte:

:: \(1kW = 1000 W\)

## Exemplos de dimensionamento
[Dimensionando de energia solar para um wdr3500]({{ "/dimensionando-de-energia-solar-para-um-wdr3500/" | relative_url }})
