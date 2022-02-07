from posixpath import split


nome = str(input('Digite seu nome Completo:')).strip()

print('Analisando seu nome...')
print('Seu nome em letras maiúsculas é {}'.format(nome.upper()))
print('Seu nome em letras minúsculas é {}'.format(nome.lower())) 
print('Seu nome ao todo tem {} letras'.format(len(nome)-nome.count(' ')))

#print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))

separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0],len(separa)))
