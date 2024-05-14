# Constantes para indexar os tuplos:
NAME,DATE,OPEN,MAX,MIN,CLOSE,VOLUME = 0,1,2,3,4,5,6

def main():
    lst = loadStockFile("nasdaq.csv")
    # Show just first and last tuples:
    print("first:", lst[0])
    print("last:", lst[-1])
    
    print("a) totVol=", totalVolume(lst))

    print("b) maxVal=", maxValorization(lst))
    
    stocksDic = stocksByDateByName(lst)
    print("c) CSCO@11:", stocksDic['2020-10-12']['CSCO'])
    print("c) AMZN@22:", stocksDic['2020-10-22']['AMZN'])

    port = {'NFLX': 100, 'CSCO': 80}
    print("d) portfolio@01:", portfolioValue(stocksDic, port, "2020-10-01"))
    print("d) portfolio@30:", portfolioValue(stocksDic, port, "2020-10-30"))

def loadStockFile(filename):
    lst = []
    with open(filename) as f:
        for line in f:
            parts = line.strip().split('\t')
            name = parts[NAME]
            date = parts[DATE]
            tup = (name, date, float(parts[OPEN]), float(parts[MAX]),
                float(parts[MIN]), float(parts[CLOSE]), int(parts[VOLUME]))
            lst.append(tup)
    return lst

def totalVolume(lst):
    totVol = {}
    
    for i in lst:
        totVol[i[NAME]]=  totVol.get(i[NAME], 0)+i[VOLUME]
        

    return totVol
def maxValorization(lst):
    vMax = {}
    maior=0
    
    for i in lst:
        maior = (i[CLOSE]/i[OPEN])*100 

        if vMax.get(i[DATE]) == None:
            vMax[i[DATE]] = (i[NAME],round(maior,2))
            
        else:
            if vMax[i[DATE]][1] < maior:
                vMax[i[DATE]] = (i[NAME],round(maior,2))
            
           
        
    return vMax

def stocksByDateByName(lst):
    dic = {}
  
    for i in lst:
        p=dic.get(i[DATE],{})
        p[i[NAME]]=i[CLOSE]
        dic[i[DATE]]=p       
    return dic
        
       

    

def portfolioValue(stocks, portfolio, date):
    assert date in stocks
    val = 0.0
    for k, v in portfolio.items():
        val+=v*stocks[date][k]

    return val

if __name__ == "__main__":
    main()
