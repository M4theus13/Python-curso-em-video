''' Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e 
o menor valor digitado e as suas respectivas posições na lista.'''
num = list()
for i in range(0,5):
    add = int(input(f'Digite um número para a posição {i}:'))
    num.append(add)
print(f'Você digitou os valores {num}')
ord = num[:]
ord.sort()
print(f'O maior valor digitado foi {ord[-1]}')
print(f'O menor valor digitado foi {ord[0]}')