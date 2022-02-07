
# Online Python - IDE, Editor, Compiler, Interpreter
from math import radians, sin, cos, tan # importando apenas o que usa não precisa referenciar com math.sin etc
angulo = float(input('Digite o ângulo que você deseja:'))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print('O ângulo de {}º têm:\nSeno de {:.2f},\nCosseno de {:.2f}\nTangente de {:.2f}'.format(angulo,seno,cosseno,tangente))