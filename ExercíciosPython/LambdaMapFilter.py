# Lambda Function
    # É uma função (pequena) sem nome
    # Pode ter vários argumentos mas somente uma expressão
    # Muito utilizada dentro de outras funções
    # Código mais 'clean'
"""
Não é necessário dar um nome à ela. Mas como não dar um nome à ela?
Podemos associá-la à uma variável, ou colocá-la dentro de uma outra função.
"""


def somar(x):
    return x + 10


print(somar(2))  # Resultado = 12


resultado = lambda x: x + 10
#      Argumento = x | Expressão x + 10
print(resultado(2))  # Resultado = 12

resultado1 = lambda x, y: x + y + 10
print(resultado1(2, 4))
"""
Mas para que usar?
    Por exemplo, se temos uma função e queremos acionar, ou multiplicar um valor à resposta daquela função
antes de retornar algo. Podemos colocar uma lambda que realize essa tarefa e ela só será executada uma vez,
e somente dentro da função onde está.
    Ela também pode ser considerada uma subfunção se colocada nessa situação.
"""

# Função lambda dentro de outra função


def somar(x):
    func2 = lambda x: x + 10
    return func2(x) * 4


print(somar(2))

# Lista de funções padrões do Python -> https://docs.python.org/3/library/functions.html

# Map Function
    # Muito utilizado em listas
    # Aplicar uma função a um Iterable, por item. (list, tuple, dic, etc)
"""
Podemos dizer também que ela mapeia um caminho que vai da função escolhida até cada
index do Iterable escolhido. Assim com a função Map conseguimos fazer com que uma função
seja aplicada à itens dentro de uma lista retornando um resultado

* Lembrar que para imprimir os valores em forma de lista é necessário converter
o resultado da função .Map
"""

lista1 = [1, 2, 3, 4]


def multi(x):
    return x * 2


lista2 = map(multi, lista1)
print(list(lista2))

# Função .map com Função Lambda:
# Usando o mesmo exemplo do anterior

print(list(map(lambda x: x * 2, lista1)))

# Filter Function
    # Muito utilizado com listas
    # Aplicar uma função a uma Iterable, filtrando os itens. (list, tuple, dic etc.)

valores = [10, 12, 34, 44, 57]


def remover20(x):
    return x > 20


# Resposta com filter
print(list(filter(remover20, valores)))
# [34, 44, 57]

# Respostas com map
print(list(map(remover20, valores)))
# [False, False, True, True, True]