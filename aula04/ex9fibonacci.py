numero=int(input("Número que desejas da sequência de Fibonacci "))

def fibonacci(n):
    f0=0
    f1=1
    if n==1:
        s=0
    elif n==2:
        s=1
    else:
        
        for i in range(1,n-1):
            s=f0+f1
            f0=f1
            f1=s

    print(s)
   
fibonacci(numero)