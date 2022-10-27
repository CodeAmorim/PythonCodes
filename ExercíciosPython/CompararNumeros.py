# Comparando numeros
n1 = int(input('Valor A: '))
n2 = int(input('Valor B: '))

if n1 > n2:
    print('O valor A é maior que o valor B')
elif n2 > n1:
    print('O valor B é maior que o valor A')
else:
    print('Não exite valor maior. Os dois são iguais')
    print(f'Valor A - {n1}')
    print(f'Valor B - {n2}')