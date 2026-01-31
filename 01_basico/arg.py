#nome = 'Luciana'
#quantidade = 5

def boas_vindas(nome,quantidade):
    print(f'Ola, {nome}')
    print(f'Temos {quantidade} Laptops em estoque')

boas_vindas('Luciana',6) # como se fosse o meu return


#deste modo posso adicionar mais de um parametro no programa 
def boas_vindas(nome,quantidade=10):
    print(f'Ola, {nome}')
    print(f'Temos {quantidade} Laptops em estoque')

boas_vindas('Joao') # como se fosse o meu return


