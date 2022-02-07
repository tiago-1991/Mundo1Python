num = int(input('Informe um número de 4 dígitos:'))

n = str(num)

print('Analisando o número {}'.format(num))
print('Unidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}'. format(n[3],n[2],n[1],n[0]))


#Não dá certo se não forem utilizados os 4 dígitos