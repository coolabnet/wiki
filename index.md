---
title: Wiki Coolab
layout: page
permalink: /
---

A **Coolab** é um coletivo que reúne diversas pessoas do Brasil com o objetivo de apoiar a construção e auxiliar nas demandas de **Redes Comunitárias**.

Esta é a documentação pública da Coolab — tutoriais, apresentações e referências sobre redes mesh, LibreMesh/LibreRouter, energia solar offgrid, serviços locais e muito mais.

## Índice

{% assign pages = site.wiki | sort: 'title' %}
{% for p in pages %}
- [{{ p.title }}]({{ p.url | relative_url }})
{% endfor %}
