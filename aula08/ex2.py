apelidos ={}

with open ("names.txt",'r') as ficheiro:
    for i in ficheiro:
        i=i.split(" ")
        i[-1] = i[-1].strip()
        if i [-1] not in apelidos:
            apelidos[i[-1]] = set()
        
        
        apelidos[i[-1]].add(i[0])
    
    for k, v in apelidos.items():
        print(f"{k} = {v}")
        
    


  
        
