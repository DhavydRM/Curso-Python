distance = float(input('Uma distância em metros: '))
km = distance / 1000
hm = distance / 100
dam = distance / 10
dm = distance * 10
cm = distance * 100
mm = distance * 1000
print('A medida de {}m equivale a \n{}km \n{}hm \n{}dam \n{}dm \n{}cm \n{}mm \n'.format(distance, km, hm, dam, dm, cm, mm))