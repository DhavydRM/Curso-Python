n1 = int(input('Número: '))
n2 = int(input('Número: '))
n3 = int(input('Número: '))
menor = n1
if n2<n1 and n2<n3:
    menor = n2
if n3<n1 and n3<n2:
    menor = n3
maior = n1
if n2>n1 and n2>n3:
    maior = n2
if n3>n1 and n3>n2:
    maior = n3
print('Maior número: {}'.format(maior))
print('Menor número: {}'.format(menor))
