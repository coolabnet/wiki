# Wiki Coolab

Documentação da [Coolab](https://coolab.org) — redes comunitárias, LibreMesh/LibreRouter, energia solar offgrid e serviços locais.

Este repositório contém o conteúdo da antiga **wiki.coolab.org** (MediaWiki 1.34.1), convertido para **Markdown** e publicado como site estático com **Jekyll** (GitHub Pages). Além do site, o dump bruto original também fica preservado aqui.

## Estrutura

| Caminho | Descrição |
| --- | --- |
| `_wiki/*.md` | **Conteúdo da wiki** (uma página por arquivo Markdown). É aqui que você edita. |
| `index.md` | Página inicial (portal com índice de todas as páginas). |
| `_layouts/`, `_config.yml`, `assets/` | Tema/configuração do site Jekyll. |
| `images/` | Arquivos enviados (uploads) da wiki original, no layout do MediaWiki. |
| `dump/wiki-dump-full.xml.gz` | Export XML bruto do MediaWiki (395 páginas, 2434 revisões). |
| `LocalSettings.php` | Configuração original da wiki (segredos removidos). |
| `tools/convert_wiki.py` | Script que converte o dump XML em `_wiki/*.md`. |

## Como editar

Edite os arquivos Markdown em `_wiki/` diretamente pelo GitHub (botão *"Editar"* / *pencil*). Ao salvar, o GitHub Pages reconstrói o site automaticamente.

- **Criar uma página nova**: adicione um arquivo `_wiki/minha-pagina.md` com:

  ```markdown
  ---
  title: "Minha Página"
  layout: page
  permalink: /minha-pagina/
  ---

  Conteúdo em Markdown…
  ```

  Ela aparece automaticamente na barra lateral e no índice da página inicial.

- **Adicionar imagens**: coloque o arquivo em `images/` e referencie assim:
  `![legenda]({{ "/images/nome-do-arquivo.jpg" | relative_url }})`

- **Fórmulas**: use `\( … \)` para LaTeX inline (renderizado por MathJax).

## Publicação

- O site é publicado pelo **GitHub Pages** a partir da branch `main`.
- URL padrão: `https://coolabnet.github.io/wiki/` (por isso `baseurl: "/wiki"` no `_config.yml`).
- Para usar um domínio próprio (ex.: `wiki.coolab.org`), troque `baseurl` para `""` no `_config.yml` e configure o domínio nas settings do Pages.

## Rodando localmente

Com Docker:

```bash
docker run --rm -p 4000:4000 -v "$PWD:/srv/jekyll" jekyll/jekyll:pages jekyll serve
# abra http://localhost:4000/wiki/
```

## Regenerar a partir do dump

O conteúdo Markdown foi gerado a partir do dump XML:

```bash
python3 tools/convert_wiki.py
```

## Origem

Dump gerado em 2026-10-16 a partir do VPS `vps-coolab` (MediaWiki 1.34.1, banco MariaDB `wikiupdate`). Extensões originais: `Translate`, `Babel`, `Scribunto`, `SimpleMathJax`, `UniversalLanguageSelector`, `CleanChanges`, `cldr`, `LocalisationUpdate` e `MarkdownExtraParser` (o texto bruto das páginas foi preservado independentemente delas).
