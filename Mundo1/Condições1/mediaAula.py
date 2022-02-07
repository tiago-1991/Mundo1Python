nota1 = float(input('Digite a primeira nota:'))
nota2 = float(input('Digite a segunda nota:'))
media = (nota1+nota2)/2

print('A sua média foi {:.1f}'.format(media))
if media >=7.0:
    print('Sua média foi boa, PARABÉNS!')
else:
    print('Sua média não foi boa. Você precisa estudar mais.')
