#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
num = int(input('Me diga um número para verificar se o número é impar ou par: '))
if num % 2 == 0:
    print('O número {} é um par'.format(num))
else:
    print('O número {} é um impar'.format(num))