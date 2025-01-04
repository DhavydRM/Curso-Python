from math import hypot

co = float(input('Cateto oposto: '))
ca = float(input('Cateto adjacente: '))
h = hypot(co, ca)
print('Hipotenusa = {:.2f}'.format(h))
