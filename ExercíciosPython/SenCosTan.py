# Digite um angulo e veja o valor do Seno, Cosseno e Tangente desse angulo
import math

ang = float(input('Digite o angulo desejado: '))
seno = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tang = math.tan(math.radians(ang))

print('Angulo {:.1f}'.format(ang))
print('Seno {:.2f}'.format(seno))
print('Cosseno {:.2f}'.format(cos))
print('Tangente {:.2f}'.format(tang))


