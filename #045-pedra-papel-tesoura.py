#Jogue jokenpô com o computador
import random
import time

#jogada maquina
m = random.randint(0,2)
if m == 0:
    escolhaMaquina = 'pedra'
elif m == 1:
    escolhaMaquina = 'papel'
else:
    escolhaMaquina = 'tesoura'

#jogada user
u = int(input('Opções:\n[0]pedra\n[1]papel\n[2]tesoura\nQual é sua jogada? '))
if u == 0:
    escolhaUser = 'pedra'
elif u == 1:
    escolhaUser = 'papel'
elif u == 2:
    escolhaUser = 'tesoura'
else:
    escolhaUser = 'valor incorreto'
    print('Valor incorreto')

print('A máquina escolheu {}'.format(escolhaMaquina))
print('O usuário escolheu {}'.format(escolhaUser))

if m == 0 and u == 0 or m == 1 and u == 1 or m == 2 and u == 2 :
    print('Empate')
elif m == 0 and u == 2 or m == 1 and u == 0 or m == 2 and u == 1 : #Maquina:Pedra Usuário:Tesoura/ Maquina:Papel Usuário:Pedra/ Maquina:Tesoura Usuário:Papel
    print('Máquina ganha')
elif m == 2 and u == 0 or m == 0 and u == 1 or m == 1 and u == 2 : #Maquina:Tesoura Usuário:Pedra/ Maquina:Pedra Usuário:Papel/ Maquina:Papel Usuário:Tesoura
    print('Usuário ganha')
else:
    print('Jogada invalida')