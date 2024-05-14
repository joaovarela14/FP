import math
def primesUpTo(n):
    numeros={x for x in range(2,n+1)}

    for i in range(2,int(math.sqrt(n))+1):
        multiplos= {x for x in range(i**2, n+1, i)}
        numeros -= multiplos
    
    return numeros

def main():
    print(primesUpTo(int(input("Número: "))))

main()
       
