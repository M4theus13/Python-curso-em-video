""" Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário 
tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário 
venceu ou perdeu."""
import random
comp = random.randint(0,5)
print('Vou pensar em um número de 0 a 5, tenta advinhar')
num = int(input('Em qual número eu pensei? '))
if comp == num:
    print('Parabéns, você acertou')
else:
    print('Ops, você errou, eu pensei no numero {}'.format(comp))