# Separando dígitos de um número
num = int(input('Digite um numero de 0 à 9999: '))
n = str(num)

print('Analisando o numero {}'.format(num))
print('Unidade: {}'.format(n[3]))
print('Dezena: {}'.format(n[2]))
print('Centena: {}'.format(n[1]))
print('Milhar: {}'.format(n[0]))