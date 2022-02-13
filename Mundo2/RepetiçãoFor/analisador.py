somaIdade = 0
mediaIdade = 0
maiorIdadeHomem = 0
nomeMaisVelho = ''
mulher20 = 0
for p in range(1,5):
    print('---- {}ª PESSOA ----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()

    somaIdade += idade
    if p ==1 and sexo in 'Mm':
        maiorIdadeHomem = idade
        nomeMaisVelho = nome
    if sexo in 'Mm' and idade > maiorIdadeHomem:
        maiorIdadeHomem = idade
        nomeMaisVelho = nome
    if sexo in 'Ff' and idade < 20:
        mulher20 += 1
mediaIdade = somaIdade/4
print('A média da idade do grupo é de {} anos'.format(mediaIdade))
print('O homem mais velho se chama {} e tem {} anos da idade.'.format(nomeMaisVelho,maiorIdadeHomem))
print('Ao todo, são {} mulheres com menos de 20 anos.'.format(mulher20))