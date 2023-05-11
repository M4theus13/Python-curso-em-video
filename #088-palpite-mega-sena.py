"""Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai 
sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta."""

from random import randint
from time import sleep
lista = list()
jogos = list()
i = int(input('Quantos sorteios será realizado? '))
tot = 0
while tot < i:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print(f'Sorteando {i} jogos')
print('Os números sorteados foram:')
for i, l in enumerate(jogos):
    print(f'Jogo {i+1} : {l}')
    sleep(1.5)