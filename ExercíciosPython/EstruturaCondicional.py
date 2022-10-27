# Radar eletrônico

vel = int(input('Digite a velocidade do carro: '))

if vel > 80:
    print('Você ultrapassou o limite de 80KM/H!')
    print('Você será multado em R$7,00 para cada KM acima do permitido')
    multa = (vel - 80) * 7
    print(f'Sua multa será de R${multa}')
else:
    print('Velocidade dentro do permitido')