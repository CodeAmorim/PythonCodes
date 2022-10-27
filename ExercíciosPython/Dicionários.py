# Dicionários
    # Utiliza index no formato de keys e Values
    # Aceita string, integer, float, boolean...
    # São mutáveis(mutables)
    # Podem ser puxados de bancos de dados também para serem manipulados

"""
Dicionários utilizam duas informações para cada dado
-- Uma key e um value --
Por exemplo, como um dicionário posso armazenar dados dos alunos de uma escola. Vários dados, aliás.
Isso leva as listas à outro patamar das listas.
"""
#         Key  - Value
aluno = {'nome': 'Ana', 'idade': 16, 'nota_final': 'A', 'aprovação': True}


print(aluno['nome'])  # Para puxar somente o nome. Não utilizamos posições, mas sim keys e values

# Atualizando itens no dicionário:
# Primeira forma:
aluno['nome'] = 'Jose'

# Segunda forma:
aluno.update({'nome': 'Pedro', 'nota_final': 'B', 'endereço': 'Rua A'})
"""
A vantagem do .update em é que é possível alterar mais de uma key ao mesmo tempo e
adicionar mais keys e values.
"""
# E se eu quiser verificar se algo existe?
print(aluno.get('sala', 'Não existe'))

"""
Utilizando o .get podemos verificar se uma determinada key existe no dicionário,
sem retornar um erro, e sim uma mensagem, que é digitada depois da virgula.
"""
# E se eu quiser remover algo?
del aluno['idade']


# Looping dentro de dicionários:
# UTILIZANDO O MESMO DICIONÁRIOS:
#   aluno = {'nome': 'Ana', 'idade': 16, 'nota_final': 'A', 'aprovação': True}

for x in aluno.keys():  # Imprime somente as keys
    print(x)

for y in aluno.values():  # Imprime somente os values
    print(y)

for z in aluno.items():  # Imprime keys e values dentro de tuples
    print(z)

for keys, values in aluno.items():  # Imprime keys e values fora da tuple
    print(keys, values)

# Visualizando itens, keys e values:

aluno1 = {'nome': 'Ana',
          'idade': 16,
          'nota_final': 'A',
          'aprovação': True,
          'Matérias': ['Física', 'Matemática', 'Inglês']
}

print(aluno1)
print(aluno1.get('Matérias'))
print(aluno1.items())
print(aluno1.keys())
print(aluno1.values())