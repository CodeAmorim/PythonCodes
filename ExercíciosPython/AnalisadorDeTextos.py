# Analisar a formatação de um texto

texto = input('Digite algo: ')

print('Está todo em letras maiúsculas - {}'.format(texto.isupper()))
print('Está todo em letras minúsculas - {}'. format(texto.islower()))
print('É feito somente de espaços - {}'.format(texto.isspace()))
print('Começando com letra maiúscula - {} '.format(texto.capitalize()))
print('É feito somente de letras - {}'.format(texto.isalpha()))
print('É feito somente de numeros - {}'.format(texto.isnumeric()))