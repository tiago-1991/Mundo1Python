from random import randint
from time import sleep
n = randint(0,5)
jogador = int(input('Pense em um número de 0 a 5: '))
print('PROCESSANDO...')
sleep(2)
if n == jogador:
    print('Íncrivel, o número pensado foi mesmo o {}. Você Venceu!'.format(n))
else:
    print('Que pena, o número pensado foi {}. Você Perdeu!'.format(n))