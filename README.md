# Wiki Coolab — dump da wiki.coolab.org

Este repositório contém um dump completo do conteúdo da wiki
[wiki.coolab.org](https://wiki.coolab.org), uma instância de
**MediaWiki 1.34.1** chamada "Wiki Coolab" (idioma `pt-br`).

## Conteúdo

| Caminho                  | Descrição                                                                 |
| ------------------------ | ------------------------------------------------------------------------- |
| `dump/wiki-dump-full.xml.gz` | Export XML do MediaWiki (`dumpBackup.php --full --uploads`): **395 páginas, 2434 revisões** e metadados de 68 arquivos enviados. |
| `images/`                | Arquivos enviados (uploads) da wiki, no layout de diretórios do MediaWiki (`images/<hash>/...`), incluindo `thumb/` (miniaturas regeneráveis), `archive/` (versões antigas) e `deleted/` (arquivos apagados). |
| `LocalSettings.php`      | Cópia da configuração da wiki para referência, com os segredos (`$wgDBpassword`, `$wgSecretKey`, `$wgUpgradeKey`) **removidos**. |

## Como restaurar

Para recriar a wiki a partir deste dump:

1. **Instale o MediaWiki 1.34.x** (a mesma versão garante compatibilidade total).
   O dump também importa em versões mais novas; se necessário, rode
   `php maintenance/update.php` depois da importação.

2. **Configure o banco e o `LocalSettings.php`**:
   use `LocalSettings.php` deste repositório como base e preencha os valores
   redactados (`$wgDBpassword`, `$wgSecretKey`, `$wgUpgradeKey`) e ajuste
   `$wgDBserver`/`$wgDBname`/`$wgDBuser` para o seu ambiente.

3. **Copie as imagens** para o diretório de uploads da nova instalação:
   ```bash
   cp -r images/* /caminho/do/mediawiki/images/
   chown -R www-data:www-data /caminho/do/mediawiki/images
   ```

4. **Importe o XML** (páginas, histórico e metadados dos uploads):
   ```bash
   cd /caminho/do/mediawiki
   php maintenance/importDump.php --uploads dump/wiki-dump-full.xml.gz
   ```

5. **Finalize** (opcional, para índices/estatísticas consistentes):
   ```bash
   php maintenance/rebuildrecentchanges.php
   php maintenance/initSiteStats.php
   php maintenance/runJobs.php
   ```

> As extensões usadas pela wiki original (`Translate`, `Babel`, `Scribunto`,
> `SimpleMathJax`, `UniversalLanguageSelector`, `CleanChanges`, `cldr`,
> `LocalisationUpdate` e `MarkdownExtraParser`) precisam ser instaladas
> separadamente para que o conteúdo seja renderizado de forma idêntica; o
> texto bruto das páginas, porém, está preservado neste dump independentemente
> das extensões.

## Origem

Dump gerado em 2026-10-16 a partir do VPS `vps-coolab`
(`/mnt/coolab_hd/coolab-server/wiki.coolab.org`), com o banco MariaDB do
container `wikicoolaborg-wiki_database-1`.
