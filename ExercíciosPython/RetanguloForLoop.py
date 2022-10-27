# Criando um retângulo com o for loop

for linha in range(20):
    print('-', end='')
print('')
for coluna in range(3):
    print('|                  |')
for linha in range(20):
    print('-', end='')
print('\n')

# Com símbolos:

linhas = 6
colunas = 6
simbolo = '@'

for l in range(linhas):
    for c in range(colunas):
        print(simbolo, end='')
    print()