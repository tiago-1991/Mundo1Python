def contador(i,f,p):
    """
    -> Faz uma contagem e mostra na tela 
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    
    by TiagoOliveira 13/04/2022
    """
    c = i
    while c<=f:
        print(f'{c} ', end='')
        c+=p
    print('FIM!')

#help(contador)
contador(0,100,10)
                                        