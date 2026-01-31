def concatenar(**palavras):
    frase = ''
    for palavra in palavras.values():
        frase += palavra + ' '
        print(frase)


concatenar(a="Nós", b="é", c="pobre")