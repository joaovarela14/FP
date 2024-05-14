def loadFile(fname, lst):
    with open(fname,'r') as ficheiro:
       for i in ficheiro:
        if i[0].isnumeric():
                value_list = i.split('\t')
                value_list[0] = int(value_list[0])
                lst.append(tuple(value_list))
    
    return lst      
            
def notafinal(reg):
    nota1 =  float (reg[-3])
    nota2 = float (reg[-2])
    nota3 = float (reg[-1])
    media = (nota1 + nota2 + nota3)/3
    return media 


def pautafinal(lst):
    print('{:6s}\t{:^55s}\t{:2s}\t'.format('Número', 'Nome', 'Nota'))
    for i in lst:
        print("{} -- {} -- {:.1f}".format(i[0],i[1],notafinal(i)))


def main():
    lst = []

    loadFile("school1.csv", lst)
    loadFile("school2.csv", lst)
    loadFile("school3.csv", lst)
    
    lst.sort()

    pautafinal(lst)
    

if __name__ == "__main__":
    main()


