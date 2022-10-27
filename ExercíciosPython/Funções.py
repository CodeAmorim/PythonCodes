# Funções
import math
from math import factorial
# DRY - Don't repeat yourself
# Parâmetro --> Argumento
# Default = Aquele que você define o valor no parâmetro. Valores pré-definidos.
# Non-Default = Aquele que você não define o valor no parâmetro.Todos os valores são passados por argumento.

"""
Porém sempre há uma ordem de precedência]
Non-Default -> Default
Ex: def boas_vindas(n, quantidade=6):
"""


# Default:
def boas_vindas(n, quantidade=6):
    nome = n.capitalize()
    print(f'Ola {nome}.')
    print(f'Temos {quantidade} laptops em estoque.')


# Non-Default:
def boas_vindas1(n, quantidade):
    nome = n.capitalize()
    print(f'Ola {nome}.')
    print(f'Temos {quantidade} laptops em estoque.')


def soma(n1, n2):
    resultado = n1 + n2
    return resultado


nome = str(input('Digite seu primeiro nome: '))
quantidade = 5

boas_vindas(nome)
boas_vindas1(nome, quantidade)

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))

print(f'A soma dos valores é {soma(n1, n2)}')

# Print e return nas funções:
"""
Funções realizam uma tarefa ou retornam valores:
"""


def cliente1(nome):
    print(f'Olá {nome}')


cliente1('Maria')


def cliente2(nome):
    return f'Olá {nome}'


cliente2('José')

"""
No chamamento das duas funções, somente uma irá imprimir o nome na tela. A função cliente1
Isso porque a função cliente1 realiza uma tarefa e a função cliente2 retorna um valor.
A função cliente2 somente retorna um valor ('Olá José') para o argumento do chamamento.
Sendo necessário assim printar a função, não somente chamá-la.
EX:
"""
print(cliente2('José'))

"""
Dessa forma a função print() irá imprimir na tela o valor que a função cliente2 carrega,
que no caso é o nome José.
"""

# Xargs - Vários argumentos numa função

# Função que soma vários números:


def soma(*numeros):  # '*' representa que a variável receberá vários argumentos
    resultado = 0
    for num in numeros:
        resultado += num
    return resultado


"""
Xargs é usada principalmente quando não sabemos qual a quantidade de argumentos que será passada
"""

x = soma(2, 3, 4, 7)
print(x)

# Importando módulos:

# Qual o fatorial de 4?
# 4 * 3 * 2 * 1 = 24

x = math.factorial(4)
print(x)