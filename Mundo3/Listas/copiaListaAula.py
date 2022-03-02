a = [2,3,4,7]
#b = a  #ao igualar duas listas, o Python cria uma ligação entre elas
b = a[:] # COPIA da Lista
b[2] = 8

print(f'Lista A: {a}')
print(f'Lista B: {b}')