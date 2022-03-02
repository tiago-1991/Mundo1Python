numeros = list()

while True:
    n = int(input('Digite um Valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso')
    else:
        print('Valores Duplicados Não São Aceitos')
    r = str(input('Quer Continuar? [S/N]'))
    if r in 'Nn':
        break 
print('-='*20)
numeros.sort()
print(f'Você digitou os valores {numeros}')
    
    