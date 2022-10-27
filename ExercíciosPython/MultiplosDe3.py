# Múltiplos de 3

soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma = soma + c
        cont += 1

print(f'A soma de todos os valores solicitados é {soma}')
print(f'Foram no total {cont} valores')