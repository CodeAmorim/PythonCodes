# Desafio If, Elif, Else

"""
Criar um programa que dependendo da temperatura (em celsius) do steak
ele retorna o ponto de cozimento em português. O usuário deverá
fornecer a temperatura.

Temperaturas - Cozimento
48ºC - Rare (Selada)
54ºC - Medium rare (Ao ponto para o mal)
60ºC - Medium (Ao ponto)
65ºC - Medium well (Ao ponto para o bem)
71ºC - Well done (Bem passada)
"""

temperatura = int(input('Qual a temperatura da carne? '))

if temperatura < 48:
    print('Cozinhar por mais alguns minutos')
elif 48 <= temperatura < 54:
    print('Selada')
elif 54 <= temperatura < 60:
    print('Ao ponto para o mal')
elif 60 <= temperatura < 65:
    print('Ao ponto')
elif 65 <= temperatura < 71:
    print('Ao ponto para o bem')
else:
    print('Bem passada')


# Segunda forma de resolver
if temperatura < 48:
    print('Cozinhar por mais alguns minutos')
elif temperatura in range(48, 53):
    print('Selada')
elif temperatura in range(54, 59):
    print('Ao ponto para o mal')
elif temperatura in range(60, 64):
    print('Ao ponto')
elif temperatura in range(65, 70):
    print('Ao ponto para o bem')
elif temperatura > 70:
    print('Bem passada')