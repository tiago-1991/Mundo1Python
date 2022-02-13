num = int(input('Digite o Primeiro Termo de uma P.A: '))
r = int(input('Digite a Razão dessa P.A: '))
decimo = num + (10 - 1) * r
for c in range(num,decimo+r,r):
    print('{}'.format(c), end=' - ')
print('ACABOU')