r1 = float(input('Digite o comprimento do Primeiro segmento em cm: '))
r2 = float(input('Digite o comprimento do Segundo segmento em cm: '))
r3 = float(input('Digite o comprimento do Terceiro segmento em cm: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos PODEM FORMAR um triângulo ', end='')
    if r1 == r2 == r3:
        print('EQUILÁTERO')
    elif r1 != r2 != r3:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('Os segmentos NÃO PODEM FORMAR um triângulo')
