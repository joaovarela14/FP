import bisect

lista_do_aço=[]
with open ('wordlist.txt','r') as ficheiro:
    for linha in ficheiro:
        lista_do_aço.append(linha.strip())

def contagem(lst,excerto):

    joao=[i[:len(excerto)] for i in lst]
    primeiro= bisect.bisect_left(joao,excerto)
    ultimo=bisect.bisect_right(joao,excerto) 

    if ultimo-primeiro!=0:
        return ultimo-primeiro
    
    else: 
        return joao[ultimo][1]

    #amo o meu joaozinho <333

print(contagem(lista_do_aço,"ea"))
print(contagem(lista_do_aço,"tb"))
