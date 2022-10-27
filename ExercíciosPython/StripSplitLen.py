# Primeiro e ultimo nome de uma pessoa
# Strip - Tira os espaços do inicio e fim da string
n = str(input('Digite seu nome completo: ')).strip()

# Split - Separa a string usando espaços como critério de separação e coloca-os em uma lista
nome = n.split()

print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(nome[0]))

# Len conta quantos itens tem na lista partindo do numero 1.
# Então aqui eu quero que ele diga qual o ultimo item da lista, utilizando a contagem de Len
print('Seu último nome é {}'.format(nome[len(nome) - 1]))