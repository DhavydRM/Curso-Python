km = int(input('Distância da viagem(km): '))
if km <= 200:
    print('Preço da passagem: R${}'.format(km*0.5))
else:
    print('Preço da passagem: R${}'.format(km*0.45))