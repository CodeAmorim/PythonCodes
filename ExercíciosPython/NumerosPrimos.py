# Números primos

num = int(input('Digite um numero: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end=' ')  # Código de cores
        tot += 1
    else:
        print('\033[31m', end=' ')  # Código de cores
    print(f'{c}', end=' ')

print(f'\n\033[mO número {num} foi divisível {tot} vezes')  # Código para parar as cores
if tot == 2:
    print('E por isso ele É PRIMO!')
else:
    print(f'E por isso ele NÃO é primo')
"""
Se o numero digitado por divisível por c -  que vai de 1 até o numero digitado - ele
irá printar em amarelo esse numero. O restante dos números ficará em vermelho.
"""