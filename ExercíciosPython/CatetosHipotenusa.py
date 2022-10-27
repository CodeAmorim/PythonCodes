# Comprimento da hipotenusa
# Toda hipotenusa é constituída pela soma dos quadrados de cada cateto. Sendo assim, a fórmula mais conhecida para o cálculo da hipotenusa é a seguinte: a² + b² = c²

cateto_oposto = float(input('Comprimento do cateto oposto: '))
cateto_adjacente = float(input('Comprimento do cateto adjacente: '))

hipotenusa = (cateto_oposto ** 2 + cateto_adjacente ** 2) ** (1/2)

print('O comprimento da hipotenusa é de {:.2f}'.format(hipotenusa))