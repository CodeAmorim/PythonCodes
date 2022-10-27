# Jogo de adivinhação
import random

print('-=-' * 20)
print('Vou pensar num numero de 0 a 5...Tente adivinhar!!')
print('-=-' * 20)

# O computador retorna um número aleatório entre 0 e 5
pc = random.randint(0, 5)

jogador = int(input('Em que numero eu pensei? '))

# Se o numero que o computador retornou é idêntico ao digitado pelo jogador, acertou.
if pc == jogador:
    print('Acertou!')
else:
    print('Errou!')
    print('Eu pensei no {}'.format(pc))