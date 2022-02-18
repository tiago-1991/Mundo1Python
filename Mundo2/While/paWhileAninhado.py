primeiro = int(input('Digite o 1º termo de uma Progressão Aritmética: '))
razao = int(input('Digite a razão dessa P.A: ' ))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais !=0:
    total += mais
    while cont <= total:
        print('{} '.format(termo),end='')
        print('-' if cont < 10 else '', end =' ')
        termo += razao
        cont += 1
    print('/ PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados'.format(total))    

    