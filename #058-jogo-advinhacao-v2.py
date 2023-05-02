""" Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o
 jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer."""
import random
comp = random.randint(0,10)
print('Vou pensar em um número de 0 a 10, tenta advinhar')
num = False
tent = 0
while comp != num:
    num = int(input('Qual é seu palpite? '))
    if comp > num:
        print('Mais... Tente novamente')
    if comp < num:
        print('Menos... Tente novamente')
    tent +=1
print('Acertou com {} tentativas, parabéns!' .format(tent))