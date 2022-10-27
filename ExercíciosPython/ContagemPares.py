# Números pares entre 1 e 50

# Primeira forma:
# Escopo(Inicio, Fim)
for n in range(1, 51):
    if n % 2 == 0:
        print(n, end=' ')
print(' \n')

# Segunda forma:
# Escopo(Inicio, Fim, Incremento)
for n in range(2, 51, 2):
    print(n, end=' ')

# Os dois loops funcionam, porém o segundo é mais sucinto, direto e ocupa menos o processador do computado.
# Utiliza de forma mais completa a ferramenta, utilizando as tres variáveis de controle do loop.
# end= ' ' - Corta a linha quando o programa encontrar o espaço ou caractere colocado entre as aspas