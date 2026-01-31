def preenche_lista(l: list) -> None:
    for volta in range(5):
        elem = input("Digite um caractere: ")
        l.append(elem)
lista = list()
preenche_lista(lista)