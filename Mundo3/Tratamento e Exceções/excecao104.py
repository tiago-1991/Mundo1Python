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

def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
                print('ERRO! Digite um número Real válido.')
                continue
        except (KeyboardInterrupt):
            print('\nEntrada de Dados interrompida pelo usuário.')
            return 0
        else:
            return n
#Principal
n1 = leiaInt('Digite um número Inteiro: ')
n2 = leiaFloat('Digite um Número Real: ')
print(f'O valor Inteiro digitado foi {n1} e o Real foi {n2}')
