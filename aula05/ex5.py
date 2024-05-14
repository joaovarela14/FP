string= str(input("String: "))
def countdigits(x):
    digitos=0
    contagem = 0
    while digitos < len(x):

       if x[digitos].isdigit() == True:

        
           contagem+=1
    
       digitos+=1
    
    return contagem


print(f'Número de digitos em {string} = {countdigits(string)}')





