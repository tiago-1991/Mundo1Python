maior = 0
menor = 0
for p in range (1,6):
    peso = float(input('Digite o peso da {}ª pessoa: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('=='*20)    
print('O Maior peso foi {:.2f}kg\nO Menor peso foi {:.2f}kg'.format(maior,menor))    
    
