def somar():
    print('Essa função vai somar valores')


def multi():
    print('Essa função vai multiplicar valores')


def find_index(to_find, item):
    for i, valor in enumerate(to_find):
        if valor == item:
            return i
    return -1

"""
Criamos um laço onde i vai girar dentro de 'to_find'. Ele vai procurar um valor dentro do 'to_find'.
Se em alguma posição ele encontrar um valor igual ao de 'to_find' na mesma posição. Ele retorna o index
E se não for retorna -1
"""