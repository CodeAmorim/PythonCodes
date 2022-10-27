# Analisador de triângulos

print('Analisador de triângulos')
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

"""
A formula que indica que 3 segmentos podem formar um triângulo é que
cada segmento precisa ser menor que a soma dos outros dois segmentos
"""
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima podem formar triângulo')
else:
    print('Os segmentos acima NÃO podem formar triângulo')