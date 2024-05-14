num=int(input("Soma de n primeiros termos? ")) -1
def leibnizPi4(n):
    soma=0
    while n>=0:
        termo = ((-1)**n)/(2*n+1)
        soma+=termo
        n-=1
       
    print(soma)

    
leibnizPi4(num)
