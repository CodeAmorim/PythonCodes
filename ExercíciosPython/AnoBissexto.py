# Dizer se o ano escrito é bissexto
ano = int(input('Que ano quer analisar: '))

# Anos bissextos são múltiplos de 4
if ano % 4 == 0:
    print(f'O ano {ano} é bissexto.')
else:
    print(f'O ano {ano} não é bissexto')