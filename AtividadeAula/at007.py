n1 = int(input('Number 1: '))
n2 = int(input('Number 2: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, \n o produto é {}, a divisão \n é {:.3f},'.format(s, m, d), end='>>>')
print(' a divisão inteira é {} e a potência é {}'.format(di, e))
