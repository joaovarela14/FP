def compareFiles(file1,file2):
    ficheiro1= open(file1,'rb')
    ficheiro_dois= open(file2,'rb')

    a=ficheiro1.read(1024)
    b=ficheiro_dois.read(1024)
    while a or b:
        
        if a != b:
            
            return ("Os ficheiros {} , {} não são iguais").format(file1,file2)

            
            
            
        else: 
            a=ficheiro1.read(1024)
            b=ficheiro_dois.read(1024)
    
    return ("Os ficheiros {} , {} são iguais").format(file1,file2)

            
    
def main():

    print(compareFiles("textonumero1.txt","numerodois.txt"))
    print(compareFiles("pg3333.txt","pg3333.txt"))

    
main()


