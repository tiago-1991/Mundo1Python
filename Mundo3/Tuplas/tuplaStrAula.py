lanche = ('Hamburguer', 'Suco', 'Pizza','Pudim','Batata Frita')

for cont in range (0,len(lanche)):
  #  print(cont) - apenas numeração dos itens
  print(f'Eu comi {lanche[cont]} na posição {cont}') # Conteúdo da tupla em string

for comida in lanche:
    print(f'Eu vou comer {comida}') # Conteúdo da tupla em string
print('Comi muito')

for comida, pos in enumerate(lanche): # mostrando posição sem o LEN 
    print(f'Eu vou comer {comida} na posição {pos}') # 
print('Comi muito')

print(sorted(lanche)) #Tupla em ordem alfabética, se transformando também em Lista
print (lanche)