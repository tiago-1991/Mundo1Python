frase = 'Curso em Vídeo Python'
print(frase[15::2])
'''print(frase.count('o'))       - buscar 'o' 

print(frase.upper().count('O'))      - ajusta toda a cadeia de caracter para maiusculo
e depois procura o 'O', achando assim todas as letras na String      

print(frase.lower().count('o'))      - ajusta toda a cadeia de caracter para minúsculo
e depois procura o 'o', achando assim todas as letras na String      

print(len(frase))        - tamanho da String com espaços

print(len(frase.strip()))       - remove espaços antes e depois

=========
print(frase.replace('Python', 'Android'))       - possibilidade de alterar a cadeia de caracter sem salvar

frase = print(frase.replace('Python', 'Android'))       - possibilidade de alterar a cadeia de caracter salvando
==========
print(""""Welcome! Are you completely new to programming?
about why and how to get started with Python""")            - para mostrar textos maiores

print('Curso' in frase)        - retorna booleano se encontra ou não a palavra solicitada na string

print(frase.find('Curso'))      - Posição inicial do 'vetor'

print(frase.split())        - separa cada palavra por listas

dividido = frase.split()        
print(dividido[0])      - exibe a primeira lista, no caso "Curso"


dividido = frase.split()        
print(dividido[2] [3])      - exibe a posição 3 da terceira lista, no caso "E"
'''  