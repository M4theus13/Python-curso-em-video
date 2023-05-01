"""Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos 
dessa progressão."""
n = int(input('Primeiro termo: '))
p = int(input('Razão: '))
d = n + (10 - 1) * p
for pa in range(n, d, p):
    print(pa, end=' ')
print('acabou')