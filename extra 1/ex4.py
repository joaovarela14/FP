def hondt(votes, numseats):
    lst=[]
    
    for i in range(len(votes)):
        lst.append(0)

    listai=votes.copy()
    new=votes.copy()
    for i in range(numseats):
        print(new)
        
        for i in range(len(new)):
            new[i] = int(votes[i]/(1+lst[i]))
                   
        maior = max(new)
        menor = 0
    
        if new.count(maior) > 1:
            for i in range(len(new)):
                if new[i] == maior:
                    if menor == 0:
                        menor = listai[i]
                    if listai[i] > menor:
                        continue
                    else: menor = listai[i]

            lst[listai.index(menor)] +=1
        else:

            lst[new.index(maior)]   +=1
         
    return lst


