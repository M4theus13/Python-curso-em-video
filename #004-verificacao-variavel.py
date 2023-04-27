#Programa que é inserido uma variavel, e ela é verificada em algumas etapas
n = input('Digite algo ')

print('é um numero? {}'.format(n.isnumeric()))
print('é alfabetico? {}' .format(n.isalpha()))
print('é alfanumerico? {}' .format(n.isalnum()))
print('tem somente letra maiuscula? {}' .format(n.isupper()))
print('tem somente letra minuscula? {}' .format(n.islower()))
print('tem somente espaços? {}' .format(n.isspace()))
print('esta captalizada? {}' .format(n.istitle()))