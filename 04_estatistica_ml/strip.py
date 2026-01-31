#remover espaços

texto = "   Ola, mundo!   "
texto = texto.strip()
print(texto)

#Removendo espaços em branco apenas do início de uma string
texto = "   Hello, mundo!   "
texto = texto.lstrip()
print(texto)

#Dividindo uma string:
texto = "Ola, Mundo!"
palavras = texto.split(",")
print(palavras) 