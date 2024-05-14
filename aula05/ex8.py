
palavra = str(input("String = "))
#A
def evenThenOdd(x):
       pares=""
       impares=""
       for i in range (len(x)):
              if i==0 or i %2==0:
                     pares+=x[i]

              else: impares+=x[i]
              
       return pares + impares

#B
def duplicados(x):
       lista = []
       
       for i in x:
              lista.append(i)
              
              
       while True:
              original=lista[:]
              i=1
              while i < len(lista):
                     if lista[i] == lista[i-1]:
                            lista.pop(i)
              
                     i+=1
              
              if original == lista:
                     break

              


       novapalavra = ""
      
       return novapalavra.join(lista)
              
              
#C

def numeros():
       numberslist=[]
       num=int(input("Número: "))
       soma=0
       for i in range(num+1):
              while soma <i:
                     numberslist.append(i)
                     soma+=1
              
              soma=0
       
       return numberslist

print(numeros())
#D

#nao consegui resolver 