primeiro = int(input('Digite o 1º termo de uma Progressão Aritmética: '))
razao = int(input('Digite a razão dessa P.A: ' ))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} '.format(termo),end='')
    print('-' if cont < 10 else '', end =' ')
    termo += razao
    cont += 1
print('/ PAUSA')

    

    