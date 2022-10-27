# Impréstimo bancário

casa = float(input('Qual o valor da casa: R$'))
salario = float(input('Qual o seu salário: R$'))
anos = float(input('Em quantos anos vai pagar: '))

prestacao = casa / (anos * 12)
limite = ((salario * 30) / 100)

if prestacao > limite:
    print('Excedeu o limite de 30% do salário')
    print('Empréstimo negado!')
    print('Casa R${:.2f}\nPrestação R${:.2f}\nLimite R${:.2f}'.format(casa, prestacao, limite))
else:
    print('Empréstimo aceito!')