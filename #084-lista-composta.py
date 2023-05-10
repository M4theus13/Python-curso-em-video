"""Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas,
guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.                                                                                                                
B) Uma listagem com as pessoas mais pesadas.                                                                                                    
C) Uma listagem com as pessoas mais leves."""

pessoas = list()
temp = list()
mai = men = 0

while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    
    if len(pessoas) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]

    pessoas.append(temp[:])
    temp.clear()
    
    n = input('deseja continuar? ')
    if n == 'n':
        break

print(f'Você cadastrou {len(pessoas)} pessoas')

print(f'O maior peso é de {mai}kg. Peso de ', end='')
for i in pessoas:
    if i[1] == mai:
        print(f'{i[0]}', end='')

print(f'\nO menor peso é de {men}kg. Peso de ', end='')
for i in pessoas:
    if i[1] == men:
        print(f'{i[0]}', end='')
