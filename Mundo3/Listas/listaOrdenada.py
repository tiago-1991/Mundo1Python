lista = []

for c in range (0,5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado ao final da Lista...')
    else:
        pos = 0 
        while pos < len(lista):
            if n<= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos} da Lista..')
                break
            pos +=1
print('-='*20)
print(f'Os valores digitados em ordem foram {lista}')