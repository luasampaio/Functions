def concatenar(**palavras):
    frase = ''
    for palavra in palavras.values():
        frase += palavra
        print(frase)

    print(concatenar(a= 'nos', b = 'somos'))


        