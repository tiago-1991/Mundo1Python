soma = cont = 0
while True:    
    num = int (input('Digite um Valor (999 para parar): '))
    if num == 999:
        break
    cont += 1
    soma += num 
print(f'A soma dos {cont} valores digitados foi {soma}')