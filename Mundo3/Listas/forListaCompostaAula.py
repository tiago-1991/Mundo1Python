galera = list()
dado = list()
totmai = totmen = 0
for c in range(0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
    
for p in galera:
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade')
        totmai +=1 
    else:
        print(f'{p[0]} é menor de idade')
        totmen +=1
        
print(f'O Total de maiores de idade foi de {totmai}, enquanto o total dos menores de idade foi de {totmen}')
        
        
