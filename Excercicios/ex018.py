from random import shuffle

p1 = str(input('Aluno 1: '))
p2 = str(input('Aluno 2: '))
p3 = str(input('Aluno 3: '))
p4 = str(input('Aluno 4: '))
lista = [p1, p2, p3, p4]
shuffle(lista)
print('A ordem de apresentação é:')
print(lista)
