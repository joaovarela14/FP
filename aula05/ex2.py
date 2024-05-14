


lista=[]
def inputFloatList():
    
    while True:
        number=input("Number: ")
        
        if number=="":
            break

        else:
            number=int(number)
            lista.append(number)

    return lista 

menor=[]
def countLower(lista,first):
    
    for i in lista:
        if first>i:
            menor.append(i)
    
    print(f"Lista de valores menores que {first}: {menor}")
    print("Número de elementos menores que {}: ".format(first),len(menor))

def minmax(lista):
    maior=lista[0]
    menor=lista[0]

    for i in lista:
        if i<menor:
            menor=i
            
        elif i>maior:
            maior = i
    
    return maior, menor
            
    
    

    
    
def media():
    media=(minmax(lista)[0] + minmax(lista)[1])/2
    print("Valor médio entre o maior e menor valor da lista: ",media)
    countLower(lista,media)
    

def main():
    inputFloatList()
    media()

main()




