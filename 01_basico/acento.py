
##Normaliza os caracteres da string para a forma de decomposição compatível (NFKD), separando os caracteres e seus diacríticos.

##unicodedata.combining(c): Verifica se o caractere é um diacrítico (como acentos). Se for, é ignorado.

import unicodedata

def remover_acento(texto):
    """
    Remove acentos de uma string.
    
    Args:
        texto (str): Texto com acentos.
        
    Returns:
        str: Texto sem acentos.
    """
    return ''.join(
        c for c in unicodedata.normalize('NFKD', texto) 
        if not unicodedata.combining(c)
    )


texto_com_acento = "Olá, como você está?"
texto_sem_acento = remover_acento(texto_com_acento)
print(texto_sem_acento)  


