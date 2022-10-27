# Reajuste salarial
salario = float(input('Digite o salario: R$'))
aumento = float(input('Aumento em %: '))

novo_salario = salario + ((salario * aumento) / 100)

print(f'Salario inicial R${salario}')
print(f'Com o aumento de {aumento}%, o novo salário ficará em R${novo_salario}')