
# Online Python - IDE, Editor, Compiler, Interpreter
nome = str(input('Qual é seu nome?'))

if nome == 'Tiago':
    print('Que Belo nome')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é Bem popular no Brasil.')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome feminino')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}!'.format(nome))
