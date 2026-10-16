---
title: "Analisando URLs usadas por aplicativos no Android"
layout: page
permalink: /analisando-urls-usadas-por-aplicativos-no-android/
---

1. Analisando URLs usadas nos aplicativos

  1. Contexto

Dado que a internet está chegando em muitos territórios e em alguns casos como um trator, atrapalhando o modo de vida e introduzindo as pessoas a vícios que elas nem imaginavam existir, alguns povos estão pedindo ajuda para filtrar os conteúdos que chegam até suas casas, restringindo alguns tipos de sites e serviços.

Para colocar os filtros em prática, precisamos saber quais URLs são utilizadas pelos sites e/ou aplicativos.

Segue um passo a passo usando o [PCAPdroid](https://play.google.com/store/apps/details?id=com.emanuelef.remote_capture&hl=en), um aplicativo para Android que não necessita de permissões extras para ser executado.

    1. Baixe o PCAPdroid

1 - Abra o Google Play Store (ou a loja de aplicativos que você usa

Busque por PCAPdroid

Instale o PCAPdroid

<figure><img src="{{ "/images/a/ac/Store-PCAPdroid.png" | relative_url }}" alt="PCAPdroid na Play Store"><figcaption>PCAPdroid na Play Store</figcaption></figure>

    1. Identificando as URLs

1 - Abra o PCAPdroid

<figure><img src="{{ "/images/4/45/Inicial-PCAPdroid.png" | relative_url }}" alt="Tela inicial do PCAPdroid"><figcaption>Tela inicial do PCAPdroid</figcaption></figure>

2 - Selecione qual aplicativo deseja analisar, por exemplo Whatsapp. Clique em voltar

<figure><img src="{{ "/images/f/ff/Apps-PCAPdroid.png" | relative_url }}" alt="Apps listados no PCAPdroid"><figcaption>Apps listados no PCAPdroid</figcaption></figure>

3 - Ao voltar a tela inicial, clique em **Ready**

<figure><img src="{{ "/images/9/95/Zap-PCAPdroid.png" | relative_url }}" alt="PCAPdroid"><figcaption>PCAPdroid</figcaption></figure>

4 - Pronto, o PCAPdroid começou a analisar quais URLs são usadas pelo Whatsapp.

Para engrossar o caldo, digo, carregar mais URLs, abra o Zap e use-o.

Mande mensagens para alguém, faça uma ligação, mande um áudio.

Volte a tela do PCAPdroid e verifique novamente a lista de URLs

<figure><img src="{{ "/images/0/07/URLs-PCAPdroid.png" | relative_url }}" alt="URLs usadas pelo Zap e capturadas no PCAPdroid"><figcaption>URLs usadas pelo Zap e capturadas no PCAPdroid</figcaption></figure>

5 - Caso queira salvar essa lista para analisar com calma

Clique no *Menu*, localizado acima e a direita (3 pontinhos)

Clique em **Save to file** e escolha onde salvar o arquivo

<figure><img src="{{ "/images/e/ec/Salvar-PCAPdroid.png" | relative_url }}" alt="Salvar URLs capturadas em um arquivo"><figcaption>Salvar URLs capturadas em um arquivo</figcaption></figure>

6 - Pronto, agora você já sabe quais URLs pode ser liberadas ou bloqueadas

Para a gestão de acessos, os projetos [guarita](https://github.com/coolabnet/guarita), [pi-hole](https://pi-hole.net/) ou [AdGuard](https://adguard.com/en/welcome.html) podem ser bons aliados.
