preco = float(input('Preço do produto: R$'))
desc = preco - (0.05 * preco)
print('Com desconto de 5%, o produto que custava {}, custa R${:.2f}'.format(preco, desc))
