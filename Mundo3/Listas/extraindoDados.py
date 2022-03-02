lista = []
while True:
    lista.append(int(input('Digite um Valor: ')))
    resp = str(input('Quer continuar?  [S/N]')).upper().strip()
    if resp in 'N':
        break
    
print('-='*20)
print(f'Você digitou {len(lista)} elementos')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
        print('O valor 5 faz parte da Lista')
else:
        print('O valor 5 NÃO faz parte da Lista')

