#  Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".

# Strip elimina os espaços
# True se os 5 primeiros dígitos de CID são idênticos à SANTO. False se não for
# Para isso ele deixa as duas strings na mesma formatação com o .upper
cid = str(input('Digite o nome de uma cidade qualquer: ')).strip()
print(cid[:5].upper() == 'SANTO')