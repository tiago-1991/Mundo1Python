def area(larg,comp):
    a = larg * comp
    print(f'A área de um terreno {larg}m x {comp}m é de {a}m².')

print('CONTROLE DE TERRENOS')
print('-='*20)
l=(float(input('LARGURA (m): ')))
c=(float(input('COMPRIMENTO (m): ')))
area(l,c)


    