r1 = float(input('Digite a Primeira reta em cm: '))
r2 = float(input('Digite a Segunda reta em cm: '))
r3 = float(input('Digite a Terceira reta em cm: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('As retas podem formar um triângulo')
else:
    print('As retas não podem formar um triângulo')