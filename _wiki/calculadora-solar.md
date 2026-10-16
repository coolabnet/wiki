---
title: "Calculadora Solar"
layout: page
permalink: /calculadora-solar/
---

<figure class="wp-block-image size-large is-resized is-style-default"><img src="https://www.coolab.org/wp-content/uploads/2021/01/calculadora_solar-1024x496.jpg" alt="" class="wp-image-1413" width="1024" height="496"/><figcaption>Calculadora solar para projetos de comunicação e informação comunitários</figcaption></figure>

Percebemos que uma das maiores barreira de adoção da energia solar está na dificuldade de acesso ao conhecimento a respeito de quais equipamentos são necessários para esses sistemas e como dimensiona-los.

Por isso com apoio da <a href="https://apc.org/">APC</a> desenvolvemos um aplicativo web que busca ajudar da forma mais intuitiva a técnicos e não-técnicos a dimensionarem seus próprios sistemas.

<h2>Como usar</h2>

<h3>1. Entenda como funciona</h3>

É importante entender que ao simplificar ao máximo as variáveis usadas em uma calculadora solar nós perdemos precisão. Então é bom entender melhor como funciona esse sistema e como é o processo de instalação.

<h3>2. Escolha os aparelhos</h3>

<figure class="wp-block-image size-large is-resized"><img src="https://www.coolab.org/wp-content/uploads/2021/01/calculadora_solar_dispositivos.jpg" alt="" class="wp-image-1422" width="580" height="313"/><figcaption>Escolha de dispositivos de comunicação</figcaption></figure>

Fizemos uma seleção dos aparelhos mais usados para redes de comunicação em malha, usando o <a rel="noreferrer noopener" href="https://gitlab.com/librerouter/librerouteros" target="_blank">Libre Router OS</a> e também alguns outros equipamentos usados para enlaces ponto-a-ponto a longa distância.

Basta selecionar os aparelhos que vão compor seu sistema e vamos usar suas informações de consumo para calcular. Também temos a opção de adicionar qualquer outro aparelho, desde que tenhamos as informações de consumo dele.

<h3>3. Defina a radiação solar do local</h3>

Disponibilizamos uma versão resumida do<a rel="noreferrer noopener" href="http://Atlas Solarimetrico do Brasil" target="_blank"> </a><a rel="noreferrer noopener" href="https://cresesb.cepel.br/publicacoes/download/Atlas_Solarimetrico_do_Brasil_2000.pdf" target="_blank">Atlas Solarimétrico do Brasil</a> para tomar como base as horas de médias de sol em diferentes estações do ano. Deve-se tomar como base o mês com menos irradiação solar, pois devemos estar prevenidos para todo o ano.

Também devemos ficar atentos com o local exato onde os aparelhos vão ser instalados, pois fatores como sombra de árvores, morros e edifícios influenciam na disponibilidade de sol.

<h3>4. Autonomia do sistema e opções</h3>

Um sistema com menos de 24 horas de autonomia é mais barato, mas não vai garantir o funcionamento dos aparelhos durante todo o tempo.

É importante observar se o local onde o sistema vai operar tem muitos dias nublados durante alguma estação do ano. Nesses casos é prudente colocar uma autonomia de alguns dias.

Das opções avançadas se deve modificar o modelo de descarga e de perda para ser mais ou menos conservador nos cálculos. Vale a pena mudar a saída do banco de baterias para usar aparelhos que precisam de 24V sem precisar de um regulador de tensão ou inversor.

<h3>5. Resultados</h3>

<figure class="wp-block-image size-large"><img src="https://www.coolab.org/wp-content/uploads/2021/01/calculadora_solar_pdf.jpg" alt="" class="wp-image-1416"/></figure>

Ao final o aplicativo mostra as especificações dos aparelhos necessários para o sistema com base nas entradas feitas pelo usuário. Ele permite compartilhar esses resultados através de uma url, e também imprimi-lo como *pdf*.

A marca dos aparelhos usados influenciam a durabilidade. No caso dos controladores de carga é importante observar nos manuais dos aparelhos se a tensão máxima dos painéis não esta acima da suportada pelo controlador.

Controladores com a tecnologia MPPT tem maior eficiência e muitas vezes valem a pena. Mas vale estar atento se o aparelho é muito barato e diz ser MPPT, pois é provavelmente falso.

Devido a diversidade de painéis disponíveis no mercado optamos por não segmenta-los em caso de sistemas com consumo superior a 400Wp. Caso uma placa não seja o suficiente para o sistema, basta comprar mais placas que somam o valor necessário em **Wp** (pico watt) e coloca-las em paralelo. Mas fique atento e entenda melhor a diferença entre ligações em série e paralelo, pois pode ser que seja necessário caso seu sistema seja grande.

<h2>Próximos passos</h2>

Acesse a calculadora em <a href="https://solar.coolab.org/">https://solar.coolab.org</a>

Nós envie sua opinião em <a href="mailto:info@coolab.org">info@coolab.org.</a>

<h2>Próximas versões</h2>

No processo de construir essa ferramenta entendemos melhor sobre as variáveis envolvidas em tais sistemas e como no futuro podemos usa-las para dar mais precisão a projetos da baixo e grande consumo.

Algumas melhorias que pensamos para uma segunda versão:

<ul><li>Calcular irradiação solar usando posição no mapa e serviço <a href="https://docs.solcast.com.au/">Solcast</a></li><li>Mais opções de equipamentos: roteadores, computadores de placa única e micro-controladores, além outros tipos de baterias e reguladores de tensão e inversores</li><li>Uma experiência mais acessível para fora do território brasileiro</li></ul>
