x = str(input("Nome: "))

def siglas(x):
    sigla=""
    for i in x:
        if i.isupper() ==  True:
            sigla+=i
    
    return sigla
    
print (siglas(x))