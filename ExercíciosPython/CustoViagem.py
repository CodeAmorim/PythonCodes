# Calcule o custo da viagem
km = int(input('Digite a distância em KM: '))

if km <= 200:
    custo = km * 0.50
    print(f'Para viagens de até 200km, cada KM sai por R$0.50')
    print(f'Sua viagem custará R${custo}')
else:
    custo = km * 0.45
    print(f'Para viagens acima de 200km, cada KM sai por R$0.45')
    print(f'Sua viagem custará R${custo}')