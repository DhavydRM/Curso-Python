vlc = int(input('Velocidade do carro(km/h): '))
if vlc > 80:
    multa = (vlc - 80) * 7
    print('Você foi multado em R${},00 reais!'.format(multa))
else: 
    print('Continue dirigindo com cuidado.')