
# Online Python - IDE, Editor, Compiler, Interpreter

import math

catOposto = float(input('Digite o comprimento do cateto oposto em cm:'))
catAdjacente = float(input('Digite o comprimento do cateto adjacente em cm:'))
hipotenusa = math.hypot(catOposto,catAdjacente)

print('o comprimento da Hipotenusa é de {:.2f}cm'.format(hipotenusa))
''' OU SEM IMPORTAÇÕES
catOposto = float(input('Digite o comprimento do cateto oposto em cm:'))
catAdjacente = float(input('Digite o comprimento do cateto adjacente em cm:'))
hipotenusa = (catOposto**2 + catAdjacente**2) **(1/2)


print('o comprimento da Hipotenusa é de {:.2f}cm'.format(hipotenusa))'''

