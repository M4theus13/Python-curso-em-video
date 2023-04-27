"""Crie um programa que leia o nome completo de uma pessoa e mostre:
O nome com todas letras maiúsculas e minúsculas.
Quantas letras ao todo sem considerar espaços.
Quantas letras tem o primeiro nome."""
nome = input('Digite seu nome completo: ')

print('Seu nome com letra maiuscula é {}'.format(nome.upper()))
print('Seu nome com letra minuscula é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
divisao = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(divisao[0], len(divisao[0])))