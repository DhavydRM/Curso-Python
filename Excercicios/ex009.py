lg = float(input('Largura da parede: '))
al = float(input('Altura da parede: '))
area = lg*al
print('A sua parede tem a dimensão de {}x{} e sua área é de {}m²'.format(lg, al, area))
print('Para pintar essa parede, você precisará de {}l de tinta.'.format(area/2))
