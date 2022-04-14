#varios parâmetros
def contador(*num):
    for valor in num:
        print(f'{valor} ', end='')
    print('FIM')

#Programa Principal
contador(2,1,7)
contador(8,0)
contador(4,4,8,4,6,8,9)

    