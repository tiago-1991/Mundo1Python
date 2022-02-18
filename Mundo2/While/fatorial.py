'''from math import factorial

n = int(input('Digite um número para calcular sem fatorial: '))
f = factorial(n)
print('O Fatorial de {} é {}'.format(n,f))'''


num = int(input('Digite um número: '))
c = num
f = 1
print('{}! = '.format(num),end = '')
while c > 0:
    print('{} '.format(c), end = '')
    print('x' if c > 1 else '=', end =' ')
    f *= c
    c -= 1 
print('{}'.format(f))
    

    