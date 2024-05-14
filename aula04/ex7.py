
a=0
soma=0
total=0
while True:
    a=(input("Valor: "))
    if a=="":
        break
    else:
        a=int(a)
        soma+=a
        total+=1
    

print("A média dos valores inseridos é igual a ",soma/total)