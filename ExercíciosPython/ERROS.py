# Erros
    # Excelentes para testes
    # Não realiza o stop no programa
    # Mensagens customizadas quando encontra um erro

"""
O que precisamos entender sobre erros?
    - Quais são os erros
    - Que tipo de erros
    E principalmente:
    - Como isolar esses erros

Existem maneiras de pular erros nos códigos para que sua execução não seja prejudicada.
E também apresentar mensagens desses erros. Mensagens essas não tão 'assustadoras'.
    Ex:
'O programa encontrou um erro'
- Um usuário está digitando seu nome e digita um número.
    Como retornar uma mensagem para ele avisando-o que o campo aceita somente letras?
"""

# Trabalhando com o Try e Except com uma lista

"""
    Imagine que você tem um programa com 500 linhas de código. Você executa e ele te retorna
um erro. Por exemplo 'index error'. Ok! Consigo entender mais ou menos em qual linhas está,
e digamos que é uma função. Que é gigante :o Ok. Como vou isolar essa função, ou essa parte do 
código para me retornar uma mensagem e deixar o código continuar para ver se funciona ou não?
Para isso você vai pedir ajuda para o TRY e EXCEPT!

"""
# Exemplo com um Index Error - Neste caso o index 3 não existe na lista

try:
    letras = ['a', 'b', 'c']
    # Index    0    1    2
    print(letras[3])
except IndexError:
    print('Index não existe')

"""
    'try' tenta a execução do código e caso o erro IndexError existir,
em 'except' ele apresenta a mensagem 'Index não existe'

    Dessa forma é possível isolar um erro, caso já tenha uma noção de que tipo
de erro está ocorrendo e continuar rodando o código. Se focando assim só na
resolução desse problema!
"""

# Erros na interação com o usuário (try e except):

"""
    Quero que o usuário digite o valor do produto que quer vender no meu site de vendas.
Ele precisa digitar o valor em um número inteiro. Não pode digitar letras
"""

try:
    valor = int(input('Digite o valor do seu produto: '))
    print(valor)
except ValueError:
    print('Favor digitar um valor em números')

# Adicionando Else e Finally:

"""
    As vezes depois que ele rode o try e se for verdadeiro ou falso, você quer que ele execute
alguma outra coisa. Você vai usar o Else. Se for falso você quer usar o Finally e apresentar
uma mensagem final ao usuário, ou gerar um código lá dentro.

- Se precisar tentar alguma coisa se a tentativa com o try for positiva, utilize o 'try' e o 'else'
- Se precisar tentar e, gerando erro ou não, você TEM que executar um outro pedaço de código, 
ou mostrar uma mensagem, ou acessar alguma coisa, abrir um arquivo, você pode colocar o 'finally' que
ele sempre vai ser executado.
"""

try:
    valor = int(input('Digite o valor do seu produto: '))
    print(valor)
except ValueError:
    print('Favor digitar um valor em números')
else:  # Só aparece se o try estiver OK!
    print('Usuário digitou um valor correto')
    resultado = valor * 2
    print(resultado)