# Cálculo de IMC - Índice de Massa Corporal

"""
Qual é a sua Altura em cm:
Qual é o seu peso em kg:
"""

# MENOR QUE 18,5    MAGREZA
# ENTRE 18,5 E 24,9 NORMAL
# ENTRE 25,0 E 29,9 SOBREPESO
# ENTRE 30,0 E 39,9 OBESIDADE
# MAIOR QUE 40,0    OBESIDADE GRAVE

altura = float(input('Qual é a sua Altura em cm: '))
peso = float(input('Qual é o seu peso em kg: '))

imc = peso / (altura/100)**2

if imc < 18.5:
    print('MAGREZA')
elif 18.5 <= imc < 25:
    print('NORMAL')
elif 25 <= imc < 30:
    print('SOBREPESO')
elif 30 <= imc < 40:
    print('OBESIDADE')
elif imc >= 40:
    print('OBESIDADE GRAVE')
