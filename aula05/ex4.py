teams=["PORTO","PSG","UNITED", "Valencia", "Casa Pia"]
defrontos=[]
def jogos(equipas):
    for i in equipas:
        for x in equipas:
            if i != x:
                defrontos.append((i,x))
     
    return defrontos 


print(jogos(teams))
        
    