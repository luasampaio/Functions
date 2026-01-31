def remover_espacos(texto):
    texto_sem_espacos = texto.replace(" ", "")
    return texto_sem_espacos

# Exemplo de uso:
frase_com_espacos = "Esta e uma frase com espacos."
frase_sem_espacos = remover_espacos(frase_com_espacos)
print(f"Frase original: '{frase_com_espacos}'")
print(f"Frase sem espacos: '{frase_sem_espacos}'")

