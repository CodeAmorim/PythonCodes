# Calcular o aumento do salário
salario = float(input('Digite o salário: R$'))

if salario > 1250:
    aumento = salario + ((10 * salario) / 100)
    print('Aumento de 10% no salário')
    print(f'O novo salário ficará em R${aumento}')
else:
    aumento = salario + ((15 * salario) / 100)
    print('Aumento de 15% no salário')
    print(f'O novo salário ficará em R${aumento}')