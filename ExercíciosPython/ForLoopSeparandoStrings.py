# Separar uma frase letra por letra

frase = str(input('DIGITE UMA FRASE: ')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)

for letra in junto:
    print(letra + ' ', end='')

print('\n')
# OU:
for letra in junto:
    print(f'{letra} ', end='')