# Parcela do produto

preco = float(input('Preço do produto: R$'))
print('''\nCondição de pagamento:
[ 1 ] - Dinheiro/cheque: 10% de desconto
[ 2 ] - À vista no cartão: 5% de desconto
[ 3 ] - Em até 2x no cartão: preço normal
[ 4 ] - 3x ou mais no cartão: 20% de juros
''')
opcao = int(input('Escolha a opção: '))

if opcao == 1:
    print('Dinheiro/cheque - 10% de desconto:')
    valor = preco - ((preco * 10) / 100)
    print(f'Valor R${valor}')
if opcao == 2:
    print('À vista no cartão: 5% de desconto:')
    valor = preco - ((preco * 5) / 100)
    print(f'Valor R${valor}')
if opcao == 3:
    print('Em até 2x no cartão: preço normal:')
    print(f'Valor R${preco}')
if opcao == 4:
    print('3x ou mais no cartão: 20% de juros')
    parcelas = int(input('Número de parcelas: '))
    valor = preco + ((preco * 20) / 100)
    print(f'Valor R${valor}')
    print(f'R${valor / parcelas} cada parcela')

