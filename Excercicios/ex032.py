casa = float(input('Valor da casa: '))
sal = float(input('Salário: '))
ano = int(input('Tempo à pagar: '))
par = casa / (ano * 12)
if par > (0.3 * sal):
    print('Empréstimo negado!')
else:
    print('Emprestimo aprovado, parcelas de R${:.2f}'.format(par))