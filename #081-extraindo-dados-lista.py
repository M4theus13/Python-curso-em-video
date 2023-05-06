"""Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista."""

num = list()
while True:
    add = int(input('Digite um valor: '))
    stop = input('deseja parar? s/n: ').upper()
    num.append(add)

    if stop == 'S':
        break

print(f'Você digitou {len(num)} números')
decres = num[:]
decres.sort(reverse=True)
print(f'Lista em ordem decrescente {decres}')


if num.index(5):
    print('O valor 5 está na lista')
else:
    print('O valor 5 não está na lista')