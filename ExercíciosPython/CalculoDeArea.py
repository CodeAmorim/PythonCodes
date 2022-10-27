# Calculo de area
larg = float(input('Digite a largura da parede: '))
alt = float(input('Digite a altura da parede: '))

m2 = larg * alt
tinta = m2 / 2

print(f'A parede tem {m2}m2')
print(f'Sendo 2 litros por m2, serão necessários {tinta} litros para pintar a parede')