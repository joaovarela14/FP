letras = dict()

with open ("pg3333.txt",'r',encoding='utf-8') as ficheiro:
    for linha in ficheiro:
        for letra in linha:
            if letra.isalpha():
                letra=letra.lower()
                if letra not in letras:
                    letras[letra] = 1
                
                else: 
                    letras[letra] += 1

for x in sorted(letras, key=lambda x: letras[x],reverse=True):
    print(x, letras[x])