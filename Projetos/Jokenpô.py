from random import randint

print('Escolha um número: ')
print('(0) Pedra \n(1) Papel \n(2) Tesoura')
player = int(input())
cpt = randint(0, 2)
if(player == cpt):
    print('Empate!')
elif(player == 0 and cpt == 1):
    print('Player wins!')
elif(player == 1 and cpt == 0):
    print('Computader wins!')
elif(player == 1 and cpt == 2):
    print('Computador wins!')
elif(player == 2 and cpt == 1):
    print('Player wins!')
elif(player == 0 and cpt == 2):
    print('Player wins!')
elif(player == 2 and cpt == 0):
    print('Computador wins!')
else:
    print('Alguem vacilou ai')
