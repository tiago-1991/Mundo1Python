n = cont = soma = 0
n = int(input('Digite um número [999 para parar]'))
while n != 999:
    cont += 1 
    soma += n
    n = int(input('Digite um número [999 para parar]'))
print('Foram digitados {} números e a soma entre eles é {}'.format(cont,soma))
print('Final do Programa')
    
            