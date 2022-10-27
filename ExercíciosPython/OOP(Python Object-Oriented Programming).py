from datetime import datetime
# OOP - Object-Oriented Programming

"""
Vamos pegar o file Matrix como exemplo.

    A grande teoria por dentro do filme é a de que você começa a entender como tudo foi criado, como
o mundo foi criado e assim por diante.
    Estou fazendo essa analogia para explicar que agora que nós vamos entrar na parte de OOP,
NÓS VAMOS CRIAR OS NOSSOS OBJETOS!
    Então agora vamos continuar utilizando os objetos do Python e começar a criar e utilizar
os nossos objetos, nossas funções. E para isso precisamos entender um pedaço do quebra-cabeças
chamado CLASSES.
"""

# Classes
    # Utilizadas para criar objetos (instances)
    # Objetos são partes dentro de uma Class (instancias)
    # Classes são utilizados para agrupar dados e funções, podendo reutilizar
    # ===
    # Class: Frutas
    # Objects: Abacate, Banana...

"""
Por exemplo. Podemos criar uma classe que vai conter duas funções contendo dados que serão reutilizadas
no código.
    Para chamar essas funções, chamamos antes a classe que às contem.

Trabalhamos com classes desde o inicio!
"""
nome = 'Tobias'
print(type(nome))
# <class 'str'> - Foi criada uma classe para depois mostrar que tipo de dado é esse
nome_lower = nome.lower()
"""
O '.' em '.lower' significa que nós estamos acessando ou criando um método
"""

# Criando a sua primeira classe
    # Aqui vamos criar uma classe que irá armazenar dados


class Funcionários:
    nome = 'Elena'
    sobrenome = 'Cabral'


usuário1 = Funcionários()

print(usuário1.nome)
print(usuário1.sobrenome)

"""
Então dessa forma acabei adicionando DADOS - 'nome' e 'sobrenome'
Criei meu objeto - 'usuário1'
E então consigo puxar esses dados utilizando o '.+nome_do_dado'

* A melhor forma de se utilizar a Classe é jogando funções lá dentro. Porque aqui nessa classe,
dessa forma, se eu tiver 1000 funcionários, imagina a quantidade de linhas de código que terei?
Não faz sentido!
"""

# Criando objetos dentro de uma classe
    # Agora vamos criar objetos e associar os parâmetros à aquele objeto dentro da classe


# Criar a classe
class Funcionários:
    pass


# Criar um objeto
usuário1 = Funcionários()
usuário2 = Funcionários()

# Criar os parâmetros do usuário1
usuário1.nome = 'Elena'
usuário1.sobrenome = 'Cabral'
usuário1.data_nascimento = '12/01/2009'

# Criar os parâmetros do usuário2
usuário2.nome = 'Carol'
usuário2.sobrenome = 'Silva'
usuário2.data_nascimento = '15/10/2005'

# Opcional
print(usuário1.nome)
print(usuário2.nome)

"""
Ainda assim nos mantemos no problema de que e se nós tivermos 1000 funcionários?
Vamos resolver esse problema em seguida.
"""

# Criando construtores
"""
O objetivo dos Constructors é reduzir a nossa passagem de parâmetros. Eu quero dar os
argumentos e passar os parâmetros de forma mais simples, sem ter que mencionar o
argumento de novo.
Ex:
    # Criar os parâmetros do usuário1
    usuário1.nome = 'Elena'
    usuário1.sobrenome = 'Cabral'
    usuário1.data_nascimento = '12/01/2009'

    # Criar os parâmetros do usuário2
    usuário2.nome = 'Carol'
    usuário2.sobrenome = 'Silva'
    usuário2.data_nascimento = '15/10/2005'

 - Reduzir toda essa passagem de parâmetros e passá-los dentro do chamamento da classe:
 EX: 'usuário1 = Funcionários('Elena')'
 
    ** IMPORTANTE:
        É necessário defini-los como argumentos ANTES de passá-los.
"""


# Criar a classe
class Funcionários:
    # Construtor:
    def __init__(self, nome, sobrenome,data_nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.data_nascimento = data_nascimento


# Criar um objeto
usuário1 = Funcionários('Elena', 'Cabral', '12/01/2009')
usuário2 = Funcionários('Carol', 'Silva', '15/10/2005')
usuário3 = Funcionários('Andre', 'Iacono', '11/03/2003')

# Opcional
print(usuário1.nome)
print(usuário2.nome)
print(usuário3.sobrenome)


"""
# Criar os parâmetros do usuário1
usuário1.nome = 'Elena'
usuário1.sobrenome = 'Cabral'
usuário1.data_nascimento = '12/01/2009'

# Criar os parâmetros do usuário2
usuário2.nome = 'Carol'
usuário2.sobrenome = 'Silva'
usuário2.data_nascimento = '15/10/2005'
"""


"""
LEGENDA:

__init__ - Função básica; Função mágica; Mandatório

Self significa que ele vai utilizar os meus 2 objetos no meu caso. Ele vai ser o objeto + '.' + argumento
    - usuário1.nome
    - usuário1.sobrenome....etc

    Então não importa quantos objetos eu tenha, na atribuição feita na função def __init__,
o objeto sempre sera trocado pelo 'self'. Terminado um objeto ele vai para o outro que está
associado à classe.
    Ou seja, o self vai girar dentro de todas os objetivos associados à classe. Atribuindo
assim os valores para os argumentos corretos.
"""

# Adicionando mais funções a classe:

 Funcionários:

    def __init__(self, nome, sobrenome,data_nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.data_nascimento = data_nascimento

    def nome_completo(self):
        return self.nome + ' ' + self.sobrenome


# Criar um objeto
usuário1 = Funcionários('Elena', 'Cabral', '12/01/2009')
usuário2 = Funcionários('Carol', 'Silva', '15/10/2005')
usuário3 = Funcionários('Andre', 'Iacono', '11/03/2003')

# Print
print(usuário1.nome + ' ' + usuário1.sobrenome)
print(Funcionários.nome_completo(usuário1))

"""
    Neste caso queremos imprimir o nome completo do usuário, porém isso se torna muito trabalhoso
num contexto onde temos 100 funcionários por exemplo.
O que fazemos então? Criamos dentro classe uma função que realize essa tarefa.
    No print, as duas funcionam, porém a segunda faz bem mais sentido para o contexto.
    
Chamamos a classe.função(argumento).

    Então o único local que mudamos é qual o usuário para ser chamado. Ao invés de criar a mesma
formatação toda vez que queremos imprimir o nome completo do funcionário na tela.
"""

# Calculando a idade do funcionário:

Funcionários:

    def __init__(self, nome, sobrenome,ano_nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.ano_nascimento = ano_nascimento

    def nome_completo(self):
        return self.nome + ' ' + self.sobrenome

    def idade_funcionario(self):
        ano_atual = datetime.now().year
        self.ano_nascimento = int(ano_atual - self.ano_nascimento)
        return self.ano_nascimento


# Criar um objeto
usuário1 = Funcionários('Elena', 'Cabral', '12/01/2009')
usuário2 = Funcionários('Carol', 'Silva', '15/10/2005')
usuário3 = Funcionários('Andre', 'Iacono', '11/03/2003')

# Print
print(usuário1.nome + ' ' + usuário1.sobrenome)
print(Funcionários.nome_completo(usuário1))
print(Funcionários.idade_funcionario(usuário1))

