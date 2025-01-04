km = float(input('Quilômetros rodados: '))
dias = int(input('Dias alugados: '))
qtdPagar = (km * 0.15) + (dias * 60)
print('O total à pagar é R${}'.format(qtdPagar))
