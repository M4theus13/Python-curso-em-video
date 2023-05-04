"""Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. 
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso."""

cont = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez',
        'onze','doze','treze','catorze','quinze','dezesseis','dezesete','dezoito','dezenove','vinte')

while True:
    n = int(input('Digite um número entre 0 e 20: '))
    if n < 0 or n > 20:
        print('Tente novamente.')
        break
    print(f'O número que você digitou foi {cont[n]}')

