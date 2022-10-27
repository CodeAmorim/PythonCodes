# Porção inteira de um numero float
import math
from math import trunc

num = float(input('Digite um número real: '))

# 1ª forma
print('A porção inteira de {} é {}'.format(num, math.trunc(num)))

# 2ª forma - Não é necessária a biblioteca math
print('A porção inteira de {} é {}'.format(num, int(num)))