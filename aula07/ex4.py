def  main():
    print("Campeonato de futebol")
    print("-"*30)
    equipas =[]

    resposta="None"
    print("Insira o nome das equipas que desejar\nPara terminar clique apenas Enter")
    print()
    while True:
        resposta =input("Equipa: ")
        if resposta !="":
            equipas.append(resposta.upper())
        
        else:
            break

    defrontos=[]
    for i in equipas:
        for x in equipas:
            if i != x:
                defrontos.append((i,x))
    
    
    print()

        
    tabela={}
    resultados={}

    for i in equipas:
        tabela[i]=[0,0,0,0,0,0]  # vitórias 0  - empates 1 -  derrotas 2 - golos marcados 3 -  golos sofridos 4  -  pontos 5
     
    
    for i in defrontos:
        print(f"RESULTADO DO JOGO {i}")
        print()
        a=int(input(f"Golos da equipa {i[0]}: "))
        b=int(input(f"Golos da equipa {i[1]}: "))
        resultados[i]=(a,b)
        print()

        tabela [i[0]][3]+=a
        tabela [i[1]][3]+=b
        tabela [i[0]][4]+=b
        tabela [i[1]][4]+=a

        if a > b:
            tabela [i[0]][0]+=1
            tabela [i[0]][5]+=3
            tabela [i[1]][2]+=1
        
        elif a < b:
            tabela [i[0]][2]+=1
            tabela [i[1]][0]+=1
            tabela [i[1]][5]+=3
        
        elif a == b:
            tabela [i[0]][1]+=1
            tabela [i[1]][1]+=1
            tabela [i[0]][5]+=1
            tabela [i[1]][5]+=1
        
    print ()
    print("-"*30)
    print("                         RESULTADOS")
    for k,v in resultados.items():
        print(f"Resultado do jogo {k[0]} vs {k[1]} --> {v}")
    
    print ()
    print("-"*30)
    print("                                    Classificação")
    print ()
    print("{:10} | {} | {} | {} | {} | {} | {}".format("Equipa", "Vitórias","Empates", "Derrotas", "Golos Marcados", "Golos Sofridos", "Pontos"))
    for k,v in tabela.items():
        print("{:10} | {:^8} | {:^7} | {:^8} | {:^14} | {:^14} | {:^6}".format(k,v[0],v[1],v[2],v[3],v[4],v[5]))

    print()

    campeao= equipas[0]
    
    for i in tabela:
        if tabela[i][5]>tabela [campeao][5]:
            campeao=i

        elif tabela [i][5] == tabela [campeao][5] and (tabela[i][3]-tabela[i][4]) > (tabela[campeao][3]-tabela[campeao][4]):
            campeao=i
           
    print()
    print("-"*30)
    print(f"O grande campeão deste campeonato é a equipa {campeao}!")
    print("-"*30)

    


main()