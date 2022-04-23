def aumentar(preco=0, taxa=0, formato=False):
    '''
    -> Calcula o aumento de um determinado preço
    retornando o resultado com ou sem formatação.
    preco:  O preco que se quer reajustar
    taxa:   A porcentagem de aumento
    formato:    Saída formatada ou não.
    return:     O valor reajustado, com ou sem formatação
    '''
    res = preco + (preco * taxa/100)
    return res if formato is False else moeda(res)

def diminuir(preco=0, taxa=0, formato=False):
    res = preco - (preco * taxa/100)
    return res if formato is False else moeda(res)

def dobro(preco=0, formato=False):
    res = preco * 2
    return res if not formato else moeda(res)

def metade(preco=0, formato=False ):
    res = preco/2
    return res if not formato else moeda(res)

def moeda(preco=0, moeda = 'R$'):
    return f'{moeda}{preco:>.2f}'.replace('.',',')

def resumo(preco=0, taxaa=10, taxar=5):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Dobro do preco: \t{dobro(preco, True)}')
    print(f'Metade do Preço: \t{metade(preco, True)}')
    print(f'{taxaa}% de Aumento: \t\t{aumentar(preco, taxaa, True)}')
    print(f'{taxar}% Desconto: \t\t{diminuir(preco, taxar, True)}')
    print('-'*30)