# Media de um aluno
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))

media = (n1 + n2) / 2

if media < 5.0:
    print('Aluno reprovado!')
    print(f'Média {media}')
elif 5.0 <= media <= 6.9:
    print('Aluno em recuperação')
    print(f'Média {media}')
elif media >= 7.0:
    print('Aluno aprovado')
    print(f'Média {media}')