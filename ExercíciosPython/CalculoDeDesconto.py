# Calculo de desconto

preco = float(input('Digite o preço do produto: R$'))
desconto = float(input('Digite o desconto em %: '))

valor_final = preco - ((desconto * preco) / 100)

print(f'Valor do produto: R${preco}')
print(f'Valor com deconto de {desconto}%: R${valor_final}')