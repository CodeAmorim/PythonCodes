# Conversor de bases numéricas
num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] Converter para binário
[ 2 ] Converter para Octal
[ 3 ] Converter para Hexadecimal''')

opcao = int(input('Sua opção: '))

if opcao == 1:
    print('{} convertido para BINÁRIO é {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} convertido para OCTAL é {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL é {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida. Tente novamente')

'''
Binário 0b + binário
Octal 0o + octal
Hexadecimal 0x + hexadecimal

!Para não aparecer o prefixo da base numérica colocamos o seguinte como cada print:
.format(num, bin(num)[2:]) -> Vai printar da segunda posição em diante
'''