"""Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. 
No final, mostre o conteúdo da estrutura na tela."""

aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))

print(f'- nome é igual a {aluno["nome"]}')
print(f'- média é igual a {aluno["media"]}')
print(f'- situação é igual a', end=' ')

if aluno['media'] >= 6:
    print(f'Aprovado')
elif aluno['media'] >= 5:
    print(f'Recuperação')
else:
    print(f'Reprovado')

