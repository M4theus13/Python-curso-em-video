#Faça um algoritimo que leia o preço de um produto e mostre seu novo preço com 5% de desconto
valor = float(input('Valor do produto: R$'))
porcentagem = float(input('Desconto: '))

desconto = porcentagem * valor / 100
valorDesconto = valor - desconto

print('O produto que custava {}, na promoção com desconto de {}% vai custar R${:.2f}'.format(valor, desconto, valorDesconto))