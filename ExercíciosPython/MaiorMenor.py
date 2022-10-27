# Maior e menor numeros
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
n3 = int(input('Terceiro valor: '))

if n1 < n2 < n3:
    menor = n3
    maior = n1
if n1 < n3 < n2:
    menor = n2
    maior = n1
if n2 < n1 < n3:
    menor = n3
    maior = n2
if n2 < n3 < n1:
    menor = n1
    maior = n2
if n3 < n1 < n2:
    menor = n2
    maior = n3
if n3 < n2 < n1:
    menor = n1
    maior = n3

print(f'O maior número é {maior}')
print(f'O menor número é {menor}')