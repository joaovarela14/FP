MONTHDAYS = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
def isLeapYear(year):
    if (year%4==0 and year%100!=0) or year%400==0:
        return True
    else:
        return False

def monthDays(year, month):

    if isLeapYear(year) == False: 
        MONTHDAYS[2]= 28                #mudança dos dias de fevereiro caso o ano seja bissexto
        
    days = MONTHDAYS[month]
    return days
    
def nextDay(year, month, day):
    diafinal=monthDays(year, month)
    if day == diafinal and month!=12:
        day=1
        month+=1
    elif month==12 and day == diafinal :
        day=1
        month=1
        year+=1
    else:
        day+=1
    
    return year,month,day

def dateIsValid(year,month,day):
    
    if month <0 or month >12 or day <0 or day > 31 or year<0:
        return False
    elif month==2 and day>28 and isLeapYear(year) == False  :
        return False
    elif month==2 and day>29 and isLeapYear(year) == True:
        return False    
    elif MONTHDAYS[month]<31 and day >30:
        return False   
    else:
         return True    


def previousday (year,month,day):
    if day==1 and month>1 and MONTHDAYS[month-1]<31 and month!=3:
        month-=1
        day=30
    
    elif day==1 and month>1 and MONTHDAYS[month-1]==31 and month!=3:
        month-=1
        day=31

    elif day==1 and month==3 and isLeapYear(year) == False:
        month-=1
        day=28

    elif day==1 and month==3 and isLeapYear(year) == True:
        month-=1
        day=29
    
    elif day==1 and month==1:
        month=12
        day=31
        year-=1
    
    else:
        day-=1
    
    return year,month,day


def main():
    ano = int(input("ano=?"))
    mes = int(input("mês=?"))
    dia = int(input("dia=?"))

    print("O ano {} foi bissexto? {} ".format(ano,isLeapYear(ano)))
    print("O mês {} tem {} dias".format(mes,monthDays(ano, mes)))
    print ("A data do dia seguinte é", nextDay(ano,mes,dia))
    print("A data {}-{}-{} é válida? {}".format(ano,mes,dia,dateIsValid(ano,mes,dia)))
    print("A data do dia anterior é", previousday(ano,mes,dia)) 

main()
    

