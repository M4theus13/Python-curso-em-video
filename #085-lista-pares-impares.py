"""Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os 
valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente."""

num = [[], []]

valor = 0
for i in range(0,7):
    valor = int(input('Digite um valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print(num)