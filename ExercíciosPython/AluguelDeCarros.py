# Aluguel de carros
# 1 dias = R$60,00 e 1 km = R$0.15
dias = int(input('Dias alugados: '))
km = float(input('Km percorridos: '))

valor = (dias * 60) + (km * 0.15)

print(f'O preço a pagar será de R${valor}')