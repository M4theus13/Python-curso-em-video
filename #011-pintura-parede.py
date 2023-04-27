"""Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta
nescessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m²"""
largura = int(input('Insira a largura: '))
altura = int(input('Insira a altura: '))

area = largura * altura
litros = area // 2

print('Será necessário {} litros de tinta para pintar uma parede com uma área de {}m²'.format(litros, area))