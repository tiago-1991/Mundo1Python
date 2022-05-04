def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
                print('ERRO! Digite um número Inteiro válido.')
                continue
        except (KeyboardInterrupt):
            print('\nEntrada de Dados interrompida pelo usuário.')
            return 0
        else:
            return n

def linha(tam = 42):
    return '-' * tam

def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c+=1
    print(linha())
    opc=leiaInt('Sua Opção: ')
    return opc