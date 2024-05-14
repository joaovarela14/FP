def loadFile(fname, lst):
    with open(fname,'r') as ficheiro:
       for i in ficheiro:
        if i[0].isnumeric():
                a = i.split('\t')
                a[0] = int(a[0])
                lst.append(tuple(a))
    
    return lst      
            
def notafinal(reg):
    nota1 =  float (reg[-3])
    nota2 = float (reg[-2])
    nota3 = float (reg[-1])
    media = (nota1 + nota2 + nota3)/3
    return media 


def pautafinal(lst):
    texto = open('tabeladenotas.txt', 'w')
    texto.write("--- PAUTA FINAL --- \n \n")
    for i in lst:
        texto.write("{} -- {} -- {:.1f}\n".format(i[0],i[1],notafinal(i)))
    

def main():
    lst = []

    loadFile("school1.csv", lst)
    loadFile("school2.csv", lst)
    loadFile("school3.csv", lst)
    
    lst.sort()

    pautafinal(lst)
    

if __name__ == "__main__":
    main()