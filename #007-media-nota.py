#Desenvolva um programa que leia duas notas de um aluno, calcule e mostre sua média.
print('Insira duas notas:')
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))

media = (nota1 + nota2) / 2

print('A média é {:.1f}'.format(media))
