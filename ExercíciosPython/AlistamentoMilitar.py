# Alistamento Militar
from datetime import date
atual = date.today().year
# date.today().year puxa o ano que está na data do computador
nascimento = int(input('Ano de nascimento: '))
idade = atual - nascimento

print('Quem nasceu em {} tem {} anos em {}'. format(nascimento, idade, atual))

if idade == 18:
    print('Você precisa se alistar IMEDIATAMENTE!')
elif idade < 18:
    print('Ainda faltam {} anos para seu alistamento'.format(18 - idade))
else:
    print('Você já deveria ter se alistado há {} anos'.format(idade - 18))
