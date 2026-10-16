---
title: "Configurando o Librerouter para o Brasil"
layout: page
permalink: /configurando-o-librerouter-para-o-brasil/
---

Receita básica para configurar o LibreRouter para as especificações da legislação brasileiras.

[Segundo a resolução n°680 que regulamenta Equipamentos de Radiocomunicação de Radiação Restrita](https://www.anatel.gov.br/legislacao/resolucoes/2017/936-resolucao-680), devemos operar nas seguintes potencias:

|Faixa (GHz) ||Canais Distintos ||Canais sem sobreposição ||Restrições de potência |
|:----------:||:---------------:||:----------------------:||:---------------------:|
|2,400 - 2,4835 ||11   ||3   ||     1W|
|5,15 – 5,35 || 8 || 8 || EIRP £ 200 mW 5
|5,47 – 5,725 || 11 || 11 || 250 mW e EIRP £ 1W|
|5,725 – 5,850 || 5 || 5 || 1W|

Assim se faz necessário Configurar o Librerouter para operar nessas faixas.

Para isso você vai precisar acessar um computador com terminal, ou um desses Putty da vida para acessar via protocolo ssh.

1- Acesso o seu roteador fazendo `ssh root@thisnode.info`

2- Agora edite o arquivo lime-community `vim /etc/config/lime-community`
 2.1- Acrescente a linha `option country 'BR'`

3- Aplique as configurações
 3.1- `lime-config && lime-apply`
