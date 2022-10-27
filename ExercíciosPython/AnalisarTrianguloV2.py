# Analisar triângulo V2

print('Analisador de triângulos')
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima podem formar triângulo')
    if r1 == r2 == r3:
        print('Será formado um Triângulo Equilátero')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('Será formado um Triângulo Isósceles')
    else:
        print('Será formado um Triângulo Escaleno')
else:
    print('Os segmentos acima NÃO podem formar triângulo')
