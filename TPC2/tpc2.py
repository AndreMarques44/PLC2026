#!/usr/bin/env python3
"""TPC2: Conversor de Markdown para HTML (Basic Syntax).

Uso:
    python3 tpc2.py ficheiro.md
    cat ficheiro.md | python3 tpc2.py
"""
import re
import sys

RE_CABECALHO = re.compile(r"(#{1,3})\s+(.*)$")
RE_ITEM_LISTA = re.compile(r"^\s*\d+\.\s+(.*)$")
RE_IMAGEM = re.compile(r"!\[([^\]]*)\]\(([^)]*)\)")
RE_LINK = re.compile(r"\[([^\]]*)\]\(([^)]*)\)")
RE_BOLD = re.compile(r"\*\*(.+?)\*\*")
RE_ITALICO = re.compile(r"\*(.+?)\*")


def converter_inline(texto):
    """Converte imagens, links, bold e itálico dentro de uma linha."""
    # Imagens antes dos links, porque ![a](b) também contém [a](b)
    texto = RE_IMAGEM.sub(r'<img src="\2" alt="\1"/>', texto)
    texto = RE_LINK.sub(r'<a href="\2">\1</a>', texto)
    # Bold antes do itálico, porque ** também contém *
    texto = RE_BOLD.sub(r'<b>\1</b>', texto)
    texto = RE_ITALICO.sub(r'<i>\1</i>', texto)
    return texto


def converter_linha(linha):
    """Converte uma linha que não pertence a uma lista."""
    m = RE_CABECALHO.match(linha)
    if m:
        nivel = len(m.group(1))
        return f'<h{nivel}>{converter_inline(m.group(2))}</h{nivel}>'
    return converter_inline(linha)


def convert(md):
    """Converte um texto em Markdown para HTML."""
    saida = []
    em_lista = False
    for linha in md.splitlines():
        m = RE_ITEM_LISTA.match(linha)
        if m:
            if not em_lista:
                saida.append('<ol>')
                em_lista = True
            saida.append(f'<li>{converter_inline(m.group(1))}</li>')
            continue
        if em_lista:
            saida.append('</ol>')
            em_lista = False
        saida.append(converter_linha(linha))
    if em_lista:
        saida.append('</ol>')
    return '\n'.join(saida)


def main():
    if len(sys.argv) > 1:
        with open(sys.argv[1], encoding='utf-8') as f:
            md = f.read()
    else:
        md = sys.stdin.read()
    print(convert(md))


if __name__ == '__main__':
    main()
