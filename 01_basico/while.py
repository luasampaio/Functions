

#produto = 
valor =  int(input( "Digite o Valor do seu Produto: "))

while valor > 20: 
    valor = (valor * 0.10) + valor
    print(f'O valor final do seu produto {valor}')
    break