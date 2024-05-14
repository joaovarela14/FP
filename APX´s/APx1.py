MONTHDAYS = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]        #lista dos dias de cada mês
def isLeapYear(year):
    if (year%4==0 and year%100!=0) or year%400==0:      #verificação se o ano é bissexto ou não
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
    
    if month <=0 or month >12 or day <=0 or day > 31 or year<0:
        return False
    elif month==2 and day>28 and isLeapYear(year) == False  :
        return False
    elif month==2 and day>29 and isLeapYear(year) == True:
        return False    
    elif MONTHDAYS[month]<31 and day >30:
        return False   
    else:
         return True    


def previousDay (year,month,day):
    if day==1 and month>1 and MONTHDAYS[month-1]<31 and month!=3:
        day=30
        month-=1
        
    
    elif day==1 and month>1 and MONTHDAYS[month-1]==31 and month!=3:
        day=31
        month-=1
        

    elif day==1 and month==3 and isLeapYear(year) == False:
        day=28
        month-=1
        

    elif day==1 and month==3 and isLeapYear(year) == True:
        day=29
        month-=1
        
    
    elif day==1 and month==1:
        day=31
        month=12
        year-=1
    
    else:
        day-=1
    
    return year,month,day


def main():
    ano = int(input("ano="))
    mes = int(input("mês="))
    dia = int(input("dia="))

    print("O ano {} foi bissexto? {} ".format(ano,isLeapYear(ano)))
    print("O mês {} tem {} dias".format(mes,monthDays(ano, mes)))
    print ("A data do dia seguinte é", nextDay(ano,mes,dia))
    print("A data introduzida é válida? {}".format(dateIsValid(ano,mes,dia)))
    print("A data do dia anterior é", previousDay(ano,mes,dia)) 

main()
    