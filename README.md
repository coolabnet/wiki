# Wiki Coolab

Documentação da Coolab — redes comunitárias, LibreMesh/LibreRouter, energia solar offgrid e serviços locais.

Site estático com **Jekyll** (GitHub Pages). Todo o conteúdo são arquivos **Markdown**.

## Adicionar ou editar uma página

Crie um arquivo em `_wiki/` — por exemplo, `_wiki/minha-pagina.md`:

````markdown
---
title: "Minha Página"
layout: page
permalink: /minha-pagina/
---

Conteúdo em Markdown…
````

A página aparece automaticamente na barra lateral e no índice da home.

- **Editar**: abra o `.md` correspondente em `_wiki/` e edite (pelo GitHub ou localmente).
- **Imagens**: coloque o arquivo em `images/` e use `![legenda]({{ "/images/nome.jpg" | relative_url }})`.
- **Fórmulas**: LaTeX inline com `\( … \)`.

## Estrutura

| Caminho | O que é |
| --- | --- |
| `_wiki/` | Páginas em Markdown — é aqui que você edita |
| `index.md` | Página inicial |
| `images/` | Imagens |
| `_layouts/`, `_config.yml`, `assets/` | Tema e configuração do site |

## Publicação

- O GitHub Pages publica a partir da branch `main` e reconstrói a cada push.
- URL padrão: `https://coolabnet.github.io/wiki/`.
- Domínio próprio (ex.: `wiki.coolab.org`): troque `baseurl` para `""` no `_config.yml`.

## Rodar localmente

```bash
docker run --rm -p 4000:4000 -v "$PWD:/srv/jekyll" jekyll/jekyll:pages jekyll serve
# abra http://localhost:4000/wiki/
```
