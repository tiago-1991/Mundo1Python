from random import randint
acertou = False
tentativas = 0
comp = randint(0,10)

while not acertou:
   num = int(input('Pense em um número entre 0 e 10 e digite-o'))
   tentativas +=1
   if num == comp:
       acertou = True
   else:
        if num > comp:
            print('O Valor é menor... Tente novamente')
        elif num < comp:
            print('O Valor é maior... Tente novamente')
print('CORRETO, o valor era {}. Acertou com {} tentativas. Parabéns'.format(num,tentativas))