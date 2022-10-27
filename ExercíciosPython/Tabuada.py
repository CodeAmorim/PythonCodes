# Tabuada

num = int(input('Digite um numero para ver a tabuada: '))

x = 1

print(f'Tabuada do {num}')
print('===============================')
while x <= 10:
    print(f'{num} x {x} = {num * x}')
    x += 1

print('===============================\n')