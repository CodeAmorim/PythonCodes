# Procurando uma string dentro de outra

nome = str(input('Qual o seu nome completo: ')).strip()

# Usamos o operador IN
print('Seu nome tem Silva? {}'.format('silva' in nome.lower()))