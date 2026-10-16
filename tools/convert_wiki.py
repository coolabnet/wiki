#!/usr/bin/env python3
"""
Converte o dump XML do MediaWiki (dump/wiki-dump-full.xml.gz) em páginas
Markdown para um site estático Jekyll.

Uso:  python3 tools/convert_wiki.py
Saída: _wiki/<slug>.md  (coleção Jekyll `wiki`)
"""
import gzip
import os
import re
import unicodedata
import xml.etree.ElementTree as ET

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DUMP = os.path.join(ROOT, "dump", "wiki-dump-full.xml.gz")
OUT = os.path.join(ROOT, "_wiki")
NS = {"m": "http://www.mediawiki.org/xml/export-0.10/"}

# ----------------------------------------------------------------------------
# Normalização
# ----------------------------------------------------------------------------

def strip_accents(s: str) -> str:
    n = unicodedata.normalize("NFD", s)
    return "".join(c for c in n if unicodedata.category(c) != "Mn")


def norm(s: str) -> str:
    """Chave de comparação: case/underscore/accent-insensitive e sem espaços."""
    s = unicodedata.normalize("NFC", s)
    s = s.replace("_", " ")
    s = strip_accents(s)
    return s.strip().casefold()


def slugify(title: str) -> str:
    s = title.replace("/", "-")           # subpáginas (ex.: /pt-br)
    s = unicodedata.normalize("NFD", s)
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    s = s.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    s = s.strip("-")
    return s or "pagina"


def escape_html(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def escape_attr(s):
    return escape_html(s).replace('"', "&quot;")


def yaml_str(s):
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


# ----------------------------------------------------------------------------
# Leitura do dump
# ----------------------------------------------------------------------------

def load_dump():
    with gzip.open(DUMP, "rt", encoding="utf-8") as f:
        root = ET.parse(f).getroot()
    pages = []  # (ns, title, text)
    for p in root.findall("m:page", NS):
        n = p.find("m:ns", NS).text or "0"
        title = p.find("m:title", NS).text or ""
        revs = p.findall("m:revision", NS)
        text = ""
        if revs:
            t = revs[-1].find("m:text", NS)
            text = t.text or "" if t is not None else ""
        pages.append((n, title, text))
    uploads = {}  # filename normalizado -> rel
    for u in root.findall(".//m:upload", NS):
        fn = (u.find("m:filename", NS).text or "").strip()
        rel = (u.find("m:rel", NS).text or "").strip()
        if fn and rel:
            uploads[norm(fn)] = rel
    return pages, uploads


# Páginas que não são conteúdo real (helpers de template/equações, redirects,
# stubs e a página default de instalação).
NOISE = {
    "!(( ", "))!", "(", ")",
    "trim", "tl", "tlb", "tlg", "str len",
    "numblk", "equationnote", "equationref",
    "markup2", "markupv", "clear", "tag",
    "basepage subpage", "when on basepage", "template link with bold",
    "documentation", "documentation subpage",
    "equationref/doc", "numblk/doc",
    "página principal", "wiki coolab", "teste",
}

def is_noise(title: str) -> bool:
    return norm(title) in {norm(x) for x in NOISE}


# ----------------------------------------------------------------------------
# Conversores de fragmentos
# ----------------------------------------------------------------------------

def internal_links(s, slug_map):
    """[[Page]] / [[Page|texto]] -> links Markdown (ou texto para red-links)."""
    def repl(m):
        target = m.group(1).strip()
        label = m.group(2).strip() if m.group(2) else None
        t = target
        t = re.sub(r"^Special:MyLanguage/", "", t, flags=re.I)
        t = re.sub(r"^Special:", "", t, flags=re.I)
        if re.match(r"^(File|Arquivo|Ficheiro|Imagem|Image|Media|Template|Predefinição|Module|Módulo|Category|Categoria):", target):
            if re.match(r"^(Category|Categoria):", target):
                return ""  # categorias são metadados
            return (label or target.split(":", 1)[1]).strip()
        key = norm(t)
        if key in slug_map:
            url = slug_map[key]
            return f"[{label or t}]({{{{ \"/{url}/\" | relative_url }}}})"
        return (label or t).strip()  # red link -> texto
    return re.sub(r"\[\[([^\]|]+)(?:\|([^\]]*))?\]\]", repl, s)


def external_links(s):
    """[http://... texto] e [//host texto] e [url] -> links Markdown."""
    def full(m):
        url, label = m.group(1), m.group(2)
        if url.startswith("//"):
            url = "https:" + url
        return f"[{label}]({url})"

    def bare(m):
        url = m.group(1)
        if url.startswith("//"):
            url = "https:" + url
        return f"[{url}]({url})"

    pat = r"(?:[a-zA-Z][\w+.-]*://|//)[^\s\]]+"
    s = re.sub(r"\[(" + pat + r")\s+([^\]]+)\]", full, s)
    s = re.sub(r"\[(" + pat + r")\]", bare, s)
    return s


def caption_text(s):
    """Limpa links de uma legenda de imagem (mantém apenas o rótulo)."""
    s = re.sub(r"\[\[([^\]|]+)(?:\|([^\]]*))?\]\]",
               lambda m: (m.group(2) or m.group(1).split(":", 1)[-1]).strip(), s)
    s = re.sub(r"\[(?:" + r"(?:[a-zA-Z][\w+.-]*://|//)[^\s\]]+" + r")\s+([^\]]+)\]", r"\1", s)
    s = re.sub(r"\[(?:" + r"(?:[a-zA-Z][\w+.-]*://|//)[^\s\]]+" + r")\]",
               lambda m: m.group(0)[1:-1], s)
    return s.strip()


ALIGN_KEYS = {"thumb", "thumbnail", "frame", "framed", "border", "left", "right",
              "center", "centre", "none", "frameless", "baseline", "middle",
              "top", "bottom", "direita", "esquerda", "centro", "direito",
              "esquerdo", "miniatura", "moldura", "borda", "semmoldura", "sem-moldura"}


def _find_image_close(s, i):
    """Localiza o `]]` que fecha um link de imagem, ignorando [[...]] e [...] aninhados."""
    dd = 0  # profundidade de [[ ]]
    sd = 0  # profundidade de [ ]
    j = i
    while j < len(s) - 1:
        two = s[j:j + 2]
        if two == "[[":
            dd += 1
            j += 2
            continue
        if two == "]]":
            if dd > 0:
                dd -= 1
                j += 2
                continue
            if sd > 0:  # um `]` fecha link externo; o próximo será reavaliado
                sd -= 1
                j += 1
                continue
            return j
        c = s[j]
        if c == "[":
            sd += 1
            j += 1
        elif c == "]":
            sd -= 1
            j += 1
        else:
            j += 1
    return -1


def images(s, uploads, images_dir):
    """[[File:X.png|...|legenda]] -> <figure>/<img>."""
    def render(body):
        if "|" in body:
            name, _, rest = body.partition("|")
        else:
            name, rest = body, ""
        name = name.strip().replace("_", " ")
        params = [p.strip() for p in rest.split("|")] if rest else []
        caption = ""
        for p in params:
            low = p.lower()
            if low in ALIGN_KEYS or re.fullmatch(r"\d+px", low):
                continue
            if p:
                caption = p
                break
        key = norm(name)
        rel = uploads.get(key)
        if not rel and images_dir:
            rel = images_dir.get(key)
        if not rel:
            return caption or f"*{name}*"
        src = f"{{{{ \"/images/{rel}\" | relative_url }}}}"
        if caption:
            clean = caption_text(caption)
            return (f'<figure><img src="{src}" alt="{escape_attr(clean)}">'
                    f"<figcaption>{escape_html(clean)}</figcaption></figure>")
        return f'<img src="{src}" alt="{escape_attr(name)}">'

    out = []
    i = 0
    opener = re.compile(r"\[\[(?:File|Arquivo|Ficheiro|Imagem|Image):")
    while True:
        m = opener.search(s, i)
        if not m:
            out.append(s[i:])
            break
        out.append(s[i:m.start()])
        close = _find_image_close(s, m.end())
        if close < 0:
            out.append(s[m.start():])
            i = len(s)
            break
        out.append(render(s[m.end():close]))
        i = close + 2
    return "".join(out)


def templates(s):
    s = re.sub(r"\{\{\s*[Cc]lear\s*\}\}", "", s)
    def note_repl(m):
        return f"> **Nota:** {m.group(1).strip()}"
    s = re.sub(r"\{\{\s*[Nn]ote\s*\|\s*([^}]*?)\s*\}\}", note_repl, s)
    # demais templates: preserva o primeiro argumento posicional
    def tmpl_repl(m):
        inner = m.group(1).strip()
        if "|" in inner:
            return inner.split("|")[0].strip()
        return ""
    s = re.sub(r"\{\{([^{}]*)\}\}", tmpl_repl, s)
    return s


def convert_lists(text):
    lines = text.split("\n")
    out = []
    for ln in lines:
        m = re.match(r"^([*#]+)\s*(.*)$", ln)
        if m:
            prefix, content = m.group(1), m.group(2)
            indent = "  " * (len(prefix) - 1)
            marker = "1. " if prefix[-1] == "#" else "- "
            out.append(indent + marker + content)
        else:
            out.append(ln)
    return "\n".join(out)


def convert_headings(text):
    def repl(m):
        content = m.group(2).strip()
        content = re.sub(r"<[^>]+>", "", content)
        content = re.sub(r"'{2,5}", "", content)
        content = re.sub(r"[*_`]", "", content)
        return "#" * len(m.group(1)) + " " + content
    return re.sub(r"^(={1,6})\s*(.*?)\s*\1\s*$", repl, text, flags=re.MULTILINE)


def cell_to_html(c):
    """Converte o conteúdo de uma célula de tabela em HTML."""
    c = c.strip()
    if "|" in c and re.match(r"^[^|]+\|(style|class|colspan|rowspan|align|width|bgcolor)\s*=", c):
        c = c.split("|", 1)[0].strip()
    s = escape_html(c)
    # bold/italic
    s = re.sub(r"'''''(.+?)'''''", r"<b><i>\1</i></b>", s)
    s = re.sub(r"'''(.+?)'''", r"<b>\1</b>", s)
    s = re.sub(r"''(.+?)''", r"<i>\1</i>", s)
    # links externos
    s = re.sub(r"\[((?:[a-zA-Z][\w+.-]*://|//)[^\s\]]+)\s+([^\]]+)\]",
               lambda m: f'<a href="{(("https:"+m.group(1)) if m.group(1).startswith("//") else m.group(1))}">{m.group(2)}</a>', s)
    # links internos
    def irepl(m):
        tgt = m.group(1).strip()
        lbl = (m.group(2) or tgt).strip()
        t = re.sub(r"^Special:MyLanguage/", "", tgt, flags=re.I)
        key = norm(t)
        if key in SLUG_MAP:
            return f'<a href="{{{{ "/{SLUG_MAP[key]}/" | relative_url }}}}">{escape_html(lbl)}</a>'
        return escape_html(lbl)
    s = re.sub(r"\[\[([^\]|]+)(?:\|([^\]]*))?\]\]", irepl, s)
    return s


def convert_table(raw):
    """Converte uma tabela MediaWiki ({| ... |}) em HTML simples."""
    caption = ""
    parts = []
    for line in raw.splitlines():
        s = line.strip()
        if s.startswith("|}"):
            continue
        if s.startswith("|+"):
            caption = s[2:].strip()
            continue
        if s.startswith("|-"):
            parts.append("</tr><tr>")
            continue
        if s.startswith("!"):
            cells = re.split(r"\s*!!\s*", s.lstrip("!"))
            parts.append("".join(f"<th>{cell_to_html(c)}</th>" for c in cells))
            continue
        if s.startswith("|"):
            cells = re.split(r"\s*\|\|\s*", s.lstrip("|"))
            parts.append("".join(f"<td>{cell_to_html(c)}</td>" for c in cells))
            continue
    body = "".join(parts)
    body = re.sub(r"<tr></tr>", "", body)
    body = re.sub(r"</tr><tr>", "</tr><tr>", body)  # mantém
    if body.startswith("</tr>"):
        body = body[len("</tr>"):]
    if body.endswith("<tr>"):
        body = body[:-len("<tr>")]
    out = "<table>"
    if caption:
        out += f"<caption>{escape_html(caption)}</caption>"
    out += "<tbody><tr>" + body + "</tr></tbody></table>"
    return out


# ----------------------------------------------------------------------------
# Conversão principal
# ----------------------------------------------------------------------------

SLUG_MAP = {}  # usado por cell_to_html


def convert(text, slug_map):
    global SLUG_MAP
    SLUG_MAP = slug_map

    text = re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)

    # protege blocos de código
    code_blocks = []
    def code_repl(m):
        lang = m.group(1) or ""
        code_blocks.append((lang, m.group(2)))
        return f"\x00CODE{len(code_blocks)-1}\x00"
    text = re.sub(
        r"<(?:pre|syntaxhighlight|source)(?:\s+lang=[\"']?([\w+-]+)[\"']?)?[^>]*>(.*?)</(?:pre|syntaxhighlight|source)>",
        code_repl, text, flags=re.DOTALL | re.IGNORECASE)

    # protege tabelas
    tables = []
    def table_repl(m):
        tables.append(convert_table(m.group(0)))
        return f"\x00TABLE{len(tables)-1}\x00"
    text = re.sub(r"\{\|.*?\|\}", table_repl, text, flags=re.DOTALL)
    # tabelas sem fechamento |} (ex.: Lista de Redes): até fim ou próximo título
    text = re.sub(r"\{\|.*?(?=\n\s*={2,6}\s|\Z)", table_repl, text, flags=re.DOTALL)

    # tags da extensão Translate e nowiki
    text = re.sub(r"<languages\s*/>", "", text, flags=re.IGNORECASE)
    text = re.sub(r"</?translate>", "", text, flags=re.IGNORECASE)
    text = re.sub(r"<tvar\b[^>]*>", "", text, flags=re.IGNORECASE)
    text = re.sub(r"</tvar>", "", text, flags=re.IGNORECASE)
    text = re.sub(r"</?poem>", "", text, flags=re.IGNORECASE)
    text = re.sub(r"<nowiki>(.*?)</nowiki>", r"\1", text, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r"</?(?:includeonly|noinclude)>", "", text, flags=re.IGNORECASE)

    text = templates(text)
    text = images(text, UPLOADS, IMAGES_DIR)
    text = internal_links(text, slug_map)
    text = external_links(text)
    text = convert_lists(text)

    # inline (antes dos títulos, para que o conteúdo destes fique limpo)
    text = re.sub(r"<math>(.*?)</math>", r"\\(\1\\)", text,
                  flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r"<code>(.*?)</code>", lambda m: f"`{m.group(1).strip()}`", text,
                  flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r"<(?:strong|b)>(.*?)</(?:strong|b)>", r"**\1**", text,
                  flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r"<(?:em|i)>(.*?)</(?:em|i)>", r"*\1*", text,
                  flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r"<br(?:\s*/?>)?", "  \n", text, flags=re.IGNORECASE)
    text = re.sub(r"</?(?:span|div|small|big|sub|sup|u|s|strike|center|font|p)\b[^>]*>", "",
                  text, flags=re.IGNORECASE)

    text = re.sub(r"'''''(.+?)'''''", r"***\1***", text, flags=re.DOTALL)
    text = re.sub(r"'''(.+?)'''", r"**\1**", text, flags=re.DOTALL)
    text = re.sub(r"''(.+?)''", r"*\1*", text, flags=re.DOTALL)

    text = convert_headings(text)
    text = re.sub(r"^----+\s*$", "---", text, flags=re.MULTILINE)

    for i, (lang, code) in enumerate(code_blocks):
        fence = "```" + lang
        text = text.replace(f"\x00CODE{i}\x00", f"{fence}\n{code.rstrip()}\n```")
    for i, html in enumerate(tables):
        text = text.replace(f"\x00TABLE{i}\x00", html)

    text = re.sub(r"[ \t]+\n", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


UPLOADS = {}
IMAGES_DIR = {}


def main():
    global UPLOADS, IMAGES_DIR
    pages, UPLOADS = load_dump()

    content = []
    for ns, title, text in pages:
        if ns == "0" and not is_noise(title):
            content.append((title, text))

    # slug único: escrita indexada pelo título exato; resolução de links por
    # chave normalizada ("último vence" para títulos que normalizam iguais).
    title_to_slug = {}
    slug_map = {}
    used = set()
    for t, _ in content:
        base = slugify(t)
        slug = base
        i = 2
        while slug in used:
            slug = f"{base}-{i}"
            i += 1
        used.add(slug)
        title_to_slug[t] = slug
        slug_map[norm(t)] = slug

    images_root = os.path.join(ROOT, "images")
    if os.path.isdir(images_root):
        for dirpath, _, filenames in os.walk(images_root):
            if any(seg in dirpath for seg in ("/thumb", "/archive", "/temp", "/deleted")):
                continue
            for fn in filenames:
                rel = os.path.relpath(os.path.join(dirpath, fn), ROOT)[len("images/"):]
                IMAGES_DIR.setdefault(norm(fn), rel)

    os.makedirs(OUT, exist_ok=True)
    for f in os.listdir(OUT):
        if f.endswith(".md"):
            os.remove(os.path.join(OUT, f))

    written = 0
    for title, text in content:
        slug = title_to_slug[title]
        md = convert(text, slug_map)
        fm = f"---\ntitle: {yaml_str(title)}\nlayout: page\npermalink: /{slug}/\n---\n\n"
        with open(os.path.join(OUT, slug + ".md"), "w", encoding="utf-8") as f:
            f.write(fm + md + "\n")
        written += 1
        if "\x00" in md:
            print("  AVISO (placeholder):", title)
    print(f"páginas convertidas: {written}")


if __name__ == "__main__":
    main()
