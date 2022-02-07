import math #FROM MATH IMPORT SQRT (CTRL ESPACO MOSTRA FUNCIONALIDADES)
num = int (input('Digite um número:'))
raiz = math.sqrt(num) # RAIZ = SQRT(NUM) CASO COMENTARIO ANTERIOR - SEM REDUNDANCIA DO 'MATH'

print('A raiz de {} é igual a {}'.format(num, math.ceil(raiz))) # CEIL arredonda para cima        

