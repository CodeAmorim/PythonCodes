# Desafio com funções

"""
Criar um programa que calcula a quantidade de tinta necessária para
pintar uma parede. O usuário deverá fornecer as seguintes
informações: Rendimento, altura e largura.
O programa deve mostrar na tela a mensagem 'Você necessita de x
latas de tinta'
"""


def calculo(rend, x, y):
    area = x * y
    latas = area / rend
    print(f'Você necessita de {latas} latas de tinta')


rendimento = int(input('Informe o rendimento em m2: '))
largura = int(input('Informe a largura da parede: '))
altura = int(input('Informe a altura da parede: '))

calculo(rendimento, largura, altura)
