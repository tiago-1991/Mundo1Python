num = int(input('Digite um número para que seja mostrada sua tabuada: '))
print('='*10)

for c in range (1,11):
    print('{} x {} = {}'.format(num,c,c*num))