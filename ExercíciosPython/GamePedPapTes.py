# Game de pedra, papel, tesoura
import random

itens = ('Pedra', 'Papel', 'Tesoura')

computador = random.randint(0, 2)
print('''ESCOLHA UMA OPÇÃO:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')

jogador = int(input('Sua jogada: '))

if computador == 0:  # Pedra
    if jogador == 0:
        print('\nEmpate')
    elif jogador == 1:
        print('\nVocê venceu')
    elif jogador == 2:
        print('\nVocê perdeu')
if computador == 1:  # Papel
    if jogador == 1:
        print('\nEmpate')
    elif jogador == 2:
        print('\nVocê venceu')
    elif jogador == 0:
        print('\nVocê perdeu')
if computador == 2:  # Tesoura
    if jogador == 2:
        print('\nEmpate')
    elif jogador == 0:
        print('\nVocê venceu')
    elif jogador == 1:
        print('\nVocê perdeu')

print(f'Você jogou {itens[jogador]}')
print(f'Ele jogou {itens[computador]}')