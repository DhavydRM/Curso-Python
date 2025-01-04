r1 = float(input('R1: '))
r2 = float(input('R2: '))
r3 = float(input('R3: '))
if (r1 + r2) > r3 and (r1 + r3) > r2 and (r2 + r3) > r1:
    print('As três retas formam um triângulo!')
else:
    print('As três retas não formam um triângulo!')