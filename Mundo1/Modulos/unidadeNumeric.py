num = int(input('Informe um número:') )
unidade = num // 1 % 10
dezena = num // 10 % 10
centena = num // 100 % 10
milhar = num // 1000 % 10
print('Analisando o número {}'.format(num))
print('Unidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}'. format(unidade, dezena, centena, milhar))