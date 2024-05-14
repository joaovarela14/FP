
# Convert a telephone number into corresponding name, if on list.
# (If not on list, just return the number itself.)
def telToName(tel, telList, nameList):
    name="None"
    for i in telList:
        if i == tel:
            name = nameList[telList.index(i)]
            break
        
        else: name = tel
    
    return name


# Return list of telephone numbers corresponding to names containing partName.
def nameToTels(partName, telList, nameList):
    numeros=[]
   
    for i in nameList:
        if partName in i:
            numeros.append(int(telList[nameList.index(i)]))

    return numeros

def main():
    # Lists of telephone numbers and names
    telList = ['975318642', '234000111', '777888333', '911911911','963234176']
    nameList = ['Angelina', 'Brad',      'Claudia',   'Bruna', 'Carolina']

    # Test telToName:
    tel = input("Tel number? ")
    print( telToName(tel, telList, nameList) )
    print( telToName('234000111', telList, nameList))
    print( telToName('222333444', telList, nameList) )

    # Test nameToTels:
    name = input("Name? ")
    print( nameToTels(name, telList, nameList) )
    print( nameToTels('Clau', telList, nameList)) #== ['777888333'] )
    print( nameToTels('Br', telList, nameList))# == ['234000111', '911911911'] )



main()
