# Estruturas de dados
# Listas[]:
    # Armazenar mais de uma informação em variáveis
    # Manter a sequência dos dados em uma variável

cidade1 = 'Rio de Janeiro'
cidade2 = 'São Paulo'
cidade3 = 'Salvador'

# LISTA
cidades = ['Rio de Janeiro', 'São Paulo', 'Salvador']
# INDEX           0               1            2

# Manipulando listas:

print(cidades[1])  # Imprime a informação do index 1; São Paulo;
print(cidades)

cidades[0] = 'Brasilia'  # Altera a informação armazenada no index 0 para Brasilia;
print(cidades)


# Funções dentro das listas:
# .append() - Adiciona uma informação ao final da lista;
cidades.append('Curitiba')
print(cidades)

# .insert() - Adiciona uma informação na posição correta escolhida;
cidades.insert(0, 'Porto Alegre')
print(cidades)

# .remove() - Remove o item idêntico ao digitado entre ();
cidades.remove('Porto Alegre')
print(cidades)

# .pop() - Remove o item da posição digitada entre ();
cidades.pop(0)
print(cidades)

# .sort() - Coloca os itens da lista em ordem alfabética;
cidades.sort()
print(cidades)


# Concatenando listas:
numeros = [2, 3, 4, 5]
letras = ['a', 'b', 'c', 'd']

lista_duplicada = numeros * 2

numeros_letras = numeros + letras
# Podemos fazer o mesmo usando a função .extend()
numeros.extend(letras)
"""
Porém nesse caso a lista 'numeros' inicial deixa de existir, dando espaço para 
a nova lista como mesmo nome e mesmo index na memoria, só que agora é uma união 
das duas listas
"""

print(lista_duplicada)
print(numeros_letras)
print(numeros)

# Listas dentro de listas:
# Podemos criar uma lista "mãe" que possui dentro dela várias outras listas

# INDEX LISTA            0                             1
supermercado = [['Sabonete', 'Shampoo'], ['Cebola', 'Fermento', 'Frango']]
# INDEX ITENS        0           1           0          1          2

"""
Neste caso temos uma lista de supermercado com 2 listas dentro dela.
A primeira lista seria de higiene pessoal e a segunda de alimentação.
"""

# Imprimindo o item 1 da primeira lista:
print(supermercado[0][0])

# Unpacking lists - Associando itens de uma lista à variáveis:

produtos = ['arroz', 'feijão', 'laranja', 'banana', 3, 5, 7, 8]

item = produtos[0]
"""
Caso eu queira armazenar cada item em uma variável, isso leva muito tempo e
muitas linhas de código
O mais rápido e fácil é fazer dessa maneira:

item1, item2, item3, item4 = produtos
print(item1)
print(item2)
print(item3)
print(item4)

Se eu não souber quantos itens existem na lista, posso fazer o seguinte:
"""
produto1, produto2, produto3, *outros = produtos  # Irá ser criada outra lista com os itens restantes na variável '*outros'

print(produto1)
print(produto2)
print(produto3)
print(outros)

# Looping dentro de uma lista
valores = [10, 20, 30, 40, 50]

for x in valores:
    print(f'O valor final do produto é {x}')

# Verificando itens em uma lista
cor_cliente = input('Digite a cor desejada: ')
cores = ['amarelo', 'verde', 'azul', 'vermelho']

if cor_cliente.lower() in cores:
    print('Cor em estoque')
else:
    print('Não temos essa cor em estoque')

# Agregando duas listas co Zip()
# Vamos fazer isso com as listas 'valores' e 'cores':

# print(zip(cores, valores)) - Irá retornar o index, portando devemos converter antes de imprimir
listas = zip(cores, valores)
print(list(listas))


# Input em uma lista
# Criar uma lista de frutas com base no que o usuário digitar

frutas_usuario = input('Digite o nome das frutas separados por virgula: ')

frutas_lista = frutas_usuario.split(', ')
print(frutas_lista)
"""
Cria uma lista dos nomes digitados. Reconhecendo cada item o que estiver entre ', '.
"""

# Tuples() - Funciona pelo mesmo propósito de uma lista, porém tem um diferença crucial.
# Não podem ser alteradas(Immutable)

cores_list = ['amarelo', 'verde', 'azul', 'vermelho']
cores_tuple = ('amarelo', 'verde', 'azul', 'vermelho')

# Arrays (Matriz)
    # Similar a listas
    # Melhor performance
    # É necessário importar o módulo
"""
Quando usar?
    Quando tiver uma enorme quantidade de itens e estiver com problemas de performance no código
"""
print()
from array import array

letras = ['a', 'b', 'c', 'd']
numeros_i = [10, 20, 30, 40]
numeros_f = [1.2, 2.2, 3.2]

print(letras)
print(numeros_i)
print(numeros_f)
print()

# Typecodes para criação de arrays -> https://docs.python.org/3/library/array.html
letras = array('u', ['a', 'b', 'c', 'd'])
numeros_i = array('i',[10, 20, 30, 40])
numeros_f = array('f', [1.2, 2.2, 3.2])

print(letras)
print(numeros_i)
print(numeros_f)

# Sets {}:
    # Similares a listas
    # Evita itens duplicados
    # Não utiliza index - Quando uma lista é convertida em Sets, ela perde a indexação. Embaralhando os itens.

"""
São usados 4 operadores:
1 - Union
2 - Difference
3 - Symmetric Diference
4 - And
"""
list1 = [10, 20, 30, 40, 50]
list2 = [10, 20, 60, 70]

num1 = set(list1)
num2 = set(list2)

print(num1 | num2)  # Union - Imprime todos valores juntos retirando os duplicados
print(num1 - num2)  # Diference - Imprime o que há em num1 que não há em num2
print(num1 ^ num2)  # Symmetric Difference - Retira os duplicados nas duas listas
print(num1 & num2)  # And - O que é há nas duas listas ao mesmo tempo

"""
A criação de um Set pode ser feito desde o inicio, sem necessidade de conversão.
Somente é necessário colocar os itens dentro de chaves:
set1 = {1, 2, 3, 4, 5}
* Criar um set vazio estará criando um dicionário, que não é a mesma coisa


Tipos de listas:

lista1 = [x, x, x, x]
array1 = array('typecode', [x, x, x, x])
tuple1 = (x, x, x, x)
set1 = {x, x, x, x}
"""

# Sets com strings:

set1 = {'a', 'b', 'c'}
set2 = {'a', 'd', 'e'}
set3 = {'c', 'd', 'f'}

# set4 = set1.union(set2) -> Retira os duplicados
# set4 = set1.difference(set3) -> Mostra a diferença entre eles
# set4 = set1.intersection(set2) -> O que tem nos dois ao mesmo tempo
# set4 = set1.symmetric_difference(set3) -> Retira todos que estão duplicados das duas listas
