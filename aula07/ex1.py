with open('lusiadas.txt', 'r', encoding="utf-8") as text:
    contagem={}
    for linha in text:
        for i in linha:
            if i.isalpha():
                i=i.lower()
                if i not in contagem:
                    contagem[i]=1
        
                else:
                    contagem[i]+=1
        


final = sorted(contagem)

for i in final:
    print(i, contagem[i])
