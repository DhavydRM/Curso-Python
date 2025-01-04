print('='*20)
nome = str(input('Qual é seu nome: '))
print('Prazer em te conhecer {:20}!'.format(nome)) #Padrão 
print('Prazer em te conhecer {:>20}!'.format(nome)) #Alinhar à direita
print('Prazer em te conhecer {:<20}!'.format(nome)) #Alinhar à esquerda
print('Prazer em te conhecer {:^20}!'.format(nome)) #Centralizar
print('Prazer em te conhecer {:=^20}!'.format(nome)) #Centralizar e preencher os espaços em branco

