# Pedaços/arquivos de códigos fora da função main para melhor organização de funções

"""
EX:
    Temos um site de ecommerce e temos funções que calculam comissões de vendedores, calculos que cuidam
de envios de e-mails e etc.
    O recomendado é separar essas funções por categoria, criando módulos que contém só as funções que
trabalham com o mesmo setor.
"""

# Importando um módulo --> 'functions.py'

from functions import somar
from functions import multi
from itens.cadastro import cliente
from functions import find_index
somar()
multi()
cliente()

list1 = ['a', 'b', 'c', 'd', 'e']

var1 = find_index(list1, 'b')
print(var1)

'''
A variável 'var1' irá armazenar o resultado da função 'find_index'.
Em find_index:
to_find é a lista
item é b
'''

"""
Import - Importa todo o módulo contendo todas as funções
'import functions'

================================================

from - Importa uma função específica do módulo e não é necessário chamar a função junto do nome
do módulo. Ex:

'from functions import somar, multi'
"""

# Criando e importando Packages
    # Packages são conjuntos de módulos

"""
Vamos criar uma pasta de nome 'itens' e criar dentro dessa pasta um arquivo de nome 'cadastro'
"""

