# List Comprehension - Strings
    # Mais simples de escrever
    # Utilizado quando você precisa criar uma nova lista a partir de uma existente
    # [expressão for item in items]

"""
"""

frutas1 = ['abacate', 'banana', 'morango', 'kiwi', 'abacaxi']
# frutas2 = []

'''for item in frutas1:
    if 'b' in item:
        frutas2.append(item)
'''
# Sintaxe -> [expressão for item in lista]
frutas2 = [item for item in frutas1 if 'k' in item]

print(frutas2)

# List Comprehension - Números

'''valores = []

for x in range(6):
    valores.append(x * 10)
'''
"""
Com list comprehensions já é possível criar um loop dentro de uma lista.
No exemplo imprimimos uma lista que os valores aumentam de 10 em 10:
"""
valores = [x * 10 for x in range(6)]
print(valores)

# Lista e Generator Expressions
    # Uma forma mais rápida para listas, dicionários etc.
    # Menos memória alocada
    # Valores em bytes
"""
Se você tem que fazer um for loop dentro de uma lista, entenda que todos os itens
daquela lista são armazenados na memória. E quando você tem pouquíssimos itens
não tem problema algum. E pouquíssimos são 2000, 3000. Mas e se você tiver itens na
casa dos milhões ou bilhões? Quanto de memória você precisa? E será que temos uma 
verão que vai gastar menos recursos dos seus servidores e máquinas que estão rodando o código?
A resposta é SIM! Se chamam GENERATOR EXPRESSIONS.
"""
"""
Lista = []
GenExp = ()
"""

from sys import getsizeof

numeros = [x * 10 for x in range(10000)]  # Lista
print(type(numeros))
print(getsizeof(numeros))  # Mostra a quantidade de memória utilizada para realizar a tarefa

print('=====')

numeros = (x * 10 for x in range(10000))  # Generator Expressions
print(type(numeros))
print(getsizeof(numeros))  # Mostra a quantidade de memória utilizada para realizar a tarefa

"""
A grande diferença do Generator Expressions para listas é a quantidade de memória utilizada
para realizar a tarefa. Rodando o código podemos ver essa diferença na impressão de getsizeof().
"""