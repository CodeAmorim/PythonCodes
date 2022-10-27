# Detector de Palíndromos

# = str(input('Digite uma frase: ')).strip().upper()
frase = 'Tobias amorim'.strip().upper()
palavras = frase.split()  # Separa numa lista a frase em palavras determinadas por espaços em branco
junto = ''.join(palavras)  # Junta todas as palavras sem espaços entre elas
inverso = ''

# len(junto) - 1 -> Pega a ultima letra da frase, no caso vai de 0 a 19
# -1, -1 -> Vai até a letra - 1, que é antes da primeira. E vai voltando uma letra. Do fim para o começo da frase
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')

# Sequencia de passo:
"""
1 - Ler a frase
2 - Tirou os espaços antes e depois e colocou tudo em maiúsculo - strip() e upper()
3 - Gerou um lista (vetor) da frase- split()
4 - Juntou tudo numa string só. Eliminando os espaços internos também - join()
5 - Criou a string inverso = '', vazia pois vai armazenar a frase ao contrário
6 - Criou um for para varrer a string:
    'for letra in range(len(junto) - 1, -1, -1):'
        Encontra a ultima posição da string ja formatada. 
        Vai até a posição -1 da string, ou seja, passo o zero.
        E vai decrementando as posições, ou seja, do fim para o inicio da string.
7 - No fim se a frase ao contrário(inverso) for idêntica à frase digitada(junto), é um palíndromo.

"""
