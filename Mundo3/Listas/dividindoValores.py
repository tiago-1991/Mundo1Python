num = []
pares = []
impares = []
while True:
    num.append(int(input('Digite um número: ')))
    resp = str(input('Quer Continuar? [S/N]'))
    if resp in 'Nn':
        break
for i, v in enumerate (num):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
print('-='*20)
print(f'A lista completa é {num}')
print(f'A lista de números pares é {pares}')
print(f'A lista de números ímpares é {impares}')
