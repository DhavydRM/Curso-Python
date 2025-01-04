#Fatiamento
frase = 'Curso em Video Python'
print(frase[0]) #Retorna o caractere 0 da frase
print(frase[0:5]) #Retorna um String que vai de 0 até 4
print(frase[0:21:2]) #Vai de 0 até 20 pulando de 2 em 2
print(frase[:14]) #Vai do começo até 13
print(frase[14:]) #Vai de 14 até o final
print(frase[0::3]) #Vai de 0 até o final pulando de 3 em 3
print(frase[::3]) #Vai do inicio até o final pulando de 3 em 3

#Analise

print(len(frase)) #Tamanho da String
print(frase.count('o')) #Conta quantos 'o' tem
print(frase.count('o',0,13)) #Conta quantos 'o' somente de 0 até indice 12
print(frase.find('deo')) #Encontrar onde começa a palavra 'deo'
print(frase.find('Android')) #Se não achar, retorna -1
print('Curso' in frase) #Retorna True se tiver essa palavra dentro da String

#Transformação

print(frase.replace('Python','Android')) #Substitui Python por Android
print(frase.upper()) #Coloca tudo em maiúscula
print(frase.lower()) #Tudo em minúscula
print(frase.capitalize()) #Só a primeira letra em maiúscula
print(frase.title()) #Primeira letra de cada palavra em maiúscula
frase1 = '   Aprenda Python  '
print(frase1.strip()) #Tira os espaço desnecessários
print(frase1.rstrip()) #Tira os espaços da direita
print(frase1.lstrip()) #Tira os espaços da esquerda

#Divisão

print(frase.split()) #Transforma cada palavra no elemento de uma lista
frase2 = (frase.split())

#Junção

print('-'.join(frase2)) #Junta todos os elementos delimitando por '-'
