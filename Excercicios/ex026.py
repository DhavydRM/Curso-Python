from random import randint

cpt = randint(1, 5)
player = int(input('Tente adivinhar meu número: '))
print('ACERTOU!' if cpt == player else 'ERROU!')
print('Eu escolhi o número {}!'.format(cpt))
