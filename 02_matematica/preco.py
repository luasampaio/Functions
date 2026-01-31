casa = float(input('qual o valor da casa? '))
sal = float(input('qual o salario do comprador '))
ano = int(input('quantos anos sera pago a emprestimo '))

quant_parc = ano * 12
val_parc = casa / quant_parc

print(f'preço da parcela:{val_parc:.2f}R$')

if val_parc >= (sal*0.70):
    print('emprestimo negado.')
else:
    print('emprestimo aprovado.')