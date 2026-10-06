"""Testes com os exemplos do enunciado do TPC2."""
from tpc2 import convert

EXEMPLOS = [
    ('# Exemplo', '<h1>Exemplo</h1>'),
    ('## Exemplo', '<h2>Exemplo</h2>'),
    ('### Exemplo', '<h3>Exemplo</h3>'),
    ('Este é um **exemplo** ...', 'Este é um <b>exemplo</b> ...'),
    ('Este é um *exemplo* ...', 'Este é um <i>exemplo</i> ...'),
    ('1. Primeiro item\n2. Segundo item\n3. Terceiro item',
     '<ol>\n<li>Primeiro item</li>\n<li>Segundo item</li>\n<li>Terceiro item</li>\n</ol>'),
    ('Como pode ser consultado em [página da UC](http://www.uc.pt)',
     'Como pode ser consultado em <a href="http://www.uc.pt">página da UC</a>'),
    ('Como se vê na imagem seguinte: ![imagem dum coelho](http://www.coellho.com) ...',
     'Como se vê na imagem seguinte: <img src="http://www.coellho.com" alt="imagem dum coelho"/> ...'),
]

if __name__ == '__main__':
    falhas = 0
    for entrada, esperado in EXEMPLOS:
        obtido = convert(entrada)
        ok = obtido == esperado
        falhas += not ok
        print('OK  ' if ok else 'FALHA', repr(entrada))
        if not ok:
            print('   esperado:', repr(esperado))
            print('   obtido:  ', repr(obtido))
    print(f'{len(EXEMPLOS) - falhas}/{len(EXEMPLOS)} testes passaram')
