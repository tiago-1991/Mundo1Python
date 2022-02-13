from datetime import date
maior = 0
menor = 0
atual = date.today().year

for c in range (1,8):
    nasc = int(input('Digite o ano em que a {}ª pessoa nasceu: '.format(c)))
    if atual - nasc < 21:
        menor += 1
    else:
        maior += 1
print('No Total, {} pessoas são maiores de idade e {} são menores'.format(maior,menor))
