"""Conversor de temperatura de C para K e F
Faça um programa que leia uma temperatura em °C e a converta para °K e °F"""
tempC = float(input('Insira uma temperatura em °C: '))

tempF = (tempC * (9/5)) + 32 
tempK = tempC + 273.15

print('A temperatura de {}°C corresponde a \nKelvin: {}°K \nFahrenheit: {}°F'.format(tempC, tempK, tempF))