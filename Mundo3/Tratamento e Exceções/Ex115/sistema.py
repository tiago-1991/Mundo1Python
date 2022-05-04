from lib.interface import *
from lib.arquivo import *
from time import sleep

arq='cursoemvideo.txt'

if  not arquivoExiste(arq):  
    criarArquivo(arq)

while True:
    resposta = menu(['Ver Pessoas Cadastradas', 'Cadastrar Nova Pessoa', 'Sair do Sistema'])
    if resposta== 1:
      # listar cotneudo de um arquivo
      lerArquivo(arq)
    elif resposta==2:
        # cadastrar nova pessoa
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq,nome,idade)
    elif resposta==3:
        sleep(.8)
        cabecalho('Saindo do Sistema....ATÉ LOGO!')
        break 
    else:
        print('ERRO!Digite uma Opção Válida')
    sleep(2)