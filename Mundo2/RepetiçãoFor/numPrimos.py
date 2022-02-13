num = int(input('Digite um número: '))
total = 0

for c in range(1,num +1):
    if num % c == 0:
        total += 1
    print('{} '. format(c), end =' ')
print ('\nO número {} foi divisível {} vezes'.format(num,total))

if total == 2:
    print('E por isso ele é PRIMO')
else:
    print('E por isso ele NÃO É PRIMO')