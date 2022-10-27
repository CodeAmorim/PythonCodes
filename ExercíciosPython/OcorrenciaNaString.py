# Econtrar o A na string do input

# Strip tira os espaços
frase = str(input('Escreva uma frase: ')).strip()

# Coloca a frase toda em MAIÚSCULO
upper = frase.upper()

# .count('A') - Quantas vezes o caractere aparece na string
print('A letra A aparece {} vezes na frase'.format(upper.count('A')))

# .find('A') - Encontra a primeira posição de incidência do A. Qual posição aparece primeiro.
print('O primeiro A aparece na posição {}'.format(upper.find('A') + 1))

# .rfind('A') - Mesma função de .find(), porém começa do fim para o inicio (r - RIGHT)
print('A última letra A aparece na posição {}'.format(upper.rfind('A') + 1))