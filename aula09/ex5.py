import bisect
lst=[]
with open ('wordlist.txt','r') as ficheiro:
    for linha in ficheiro:
        lst.append(linha.strip())

def escritasmart (lst,excerto):
    joao=[i[:len(excerto)] for i in lst]
    primeiro= bisect.bisect_left(joao,excerto)
    ultimo=bisect.bisect_right(joao,excerto)    
    resposta=[]
    
    for i in range (primeiro,ultimo):
        resposta.append(lst[i][len(excerto):])
        
    print(resposta)

def main():
    exc=input("Excerto: ")
    escritasmart(lst,exc)


main()