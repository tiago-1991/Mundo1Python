s = 0
cont = 0
for c in range(1,501,2):
    if c % 3 == 0:
        cont += 1
        s += c
print('A soma entre todos os {} números Ímpares e múltilos de 3 entre 1 e 500 é {}'.format(cont,s))
