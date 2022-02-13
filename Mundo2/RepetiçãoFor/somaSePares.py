s = 0
cont = 0

for c in range (1,7):
    num = int(input('Digite um valor Para a Soma:'))
    if num % 2 == 0:
        s += num
        cont +=1
print('A soma Total dos {} números pares digitados é {}'.format(cont,s))
        