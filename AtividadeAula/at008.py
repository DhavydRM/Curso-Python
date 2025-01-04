#import math => importa toda a biblioteca
#from math import sqrt => importa só uma funcionalidade da biblioteca
from math import sqrt, ceil, floor

num = int(input('Digite um number: '))
raiz = sqrt(num)
print('A raiz quadradad de {} é {}'.format(num, ceil(raiz))) #Arredonda a raiz quadrada pra cima
print('A raiz quadradad de {} é {}'.format(num, floor(raiz))) #Arredonda a raiz quadrada pra baixo
