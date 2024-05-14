def isPrime(k):
    resto=0
    
    for i in range( 1,k+1):
        if k%i==0:
            resto+=1
    
    return resto ==2
              
for i in range(1,101):
    print("O número {} é primo? {}".format(i,isPrime(i)))

