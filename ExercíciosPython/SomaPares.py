# Soma dos números pares
soma = 0
for c in range(6):
    num = int(input('Digite um numero: '))
    if num % 2 == 0:
        soma = soma + num

print(f'A soma dos valores pares é {soma}')
