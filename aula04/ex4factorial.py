x=int(input("n= "))

def factorial(n):
    resultado=1
    for i in range (1,n+1):
        resultado = i* resultado
    
    print("O factorial do número {} é {}".format(n,resultado))

factorial(x)

