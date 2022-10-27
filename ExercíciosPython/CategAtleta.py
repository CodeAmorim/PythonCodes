# Categoria de um atleta
from datetime import date
atual = date.today().year
nascimento = int(input('Ano de nascimento: '))
idade = atual - nascimento

if idade <= 9:
    print('Categoria Mirim')
    print(f'Idade {idade}')
elif 9 < idade <= 14:
    print('Categoria Infantil')
    print(f'Idade {idade}')
elif 14 <= idade <= 19:
    print('Categoria Junior')
    print(f'Idade {idade}')
elif 19 <= idade <= 25:
    print('Categoria Sênior')
    print(f'Idade {idade}')
elif idade > 25:
    print('Categoria Master')
    print(f'Idade {idade}')
