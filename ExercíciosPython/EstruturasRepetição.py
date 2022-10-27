# Estruturas de repetição

# For loop - é utilizado quando você não sabe qual o tamanho do loop
# Imprimir de 0 a 10:
for numero in range(11):
    print(numero, end=' ')

print('\n')
# Imprimir de 1 à 10:
for numero in range(1, 11):
    print(numero, end=' ')

print('\n')
# Imprimir de 0 à 20 somente os pares:
print('Pares de 0 a 20:')
for numero in range(0, 21, 2):
    print(numero, end=' ')

print('\n')
# Imprimir de 0 à 20 somente os ímpares:
print('Impares de 0 a 20:')
for numero in range(1, 20, 2):
    print(numero, end=' ')

print('\n')
# Imprimir de 20 até 0:
print('Contagem regressiva:')
for numero in range(20, -1, -1):
    print(numero, end=' ')

print('\n')
numero = 20
# # Imprimir de 20 até 0:
print('Contagem regressiva: ')
while numero >= 0:
    print(numero, end=' ')
    numero -= 1

print('\n')
palavra = 'Google'
for letra in palavra:
    print(letra, end=' ')


