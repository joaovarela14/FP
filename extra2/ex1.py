def validarnumero(numero):
    if numero[0].isdigit() or numero[0] == '+':
        if (numero[0] == '+' and 3<= len(numero[1:])<=9) or (numero[0] != '+' and 2<= len(numero[1:])<=8):
            for i in numero[1:]:
                if i.isdigit() == False:
                    return False
            return True   
        return False
    return False 

def registarchamada():
    t1 = '0'
    t2 = '0'
    while validarnumero(t1) == False:
        t1=input('Telefone origem? ')

    while validarnumero(t2) == False:
        t2=input('Telefone destino? ')
    
    duracao= int(input('Duração (s)? '))

def lerficheiro(name):
    registo=[]
    with open (name,'r') as file:
        for line in file:
            registo.append(line.split())
    return registo

def listarclientes(lista):
    clientes = set()
    for i in lista:
        clientes.add(i[0])

    
    return clientes if len(clientes)>0 else 'Sem ficheiro associado \nExecute a opção 2 do menu'

def fatura():
    cliente = input('Cliente? ')

    print('Fatura do cliente', cliente)

    print('Destino                Duração             Custo')
    total=0
    for i in lerficheiro('chamadas1.txt'):

        if i[0] == cliente:
            if i[1][0] == '2':
                custo = 0.02
            elif i[1][0] == '+':
                custo = 0.80
            elif i[1][0] == i[0][0] and i[1][1]== i[0][1]:
                custo = 0.04
            else:
                custo = 0.10
            
            preco=(int(i[2])/60)*custo
            total+=preco
            print('{:<12}{:>18}              {:.2f}'.format(i[1],i[2],preco))
    print('                                    Total: {:.2f}'.format(total))


def menu():
    
    print('1) Registar chamada')
    print('2) Ler ficheiro')
    print('3) Listar clientes')
    print('4) Fatura')
    print('5) Terminar')
    op = input('Opção? ')

    return op



def main():
    op = None
    lista=[]
    while op != '5':
        print('-'*30)
        op=menu()
        if op == "5":
            print("Fim")
            
        elif op == "1":
            print("Operação: Registar chamada")
            print('-'*30)
            registarchamada()

        elif op == "2":
            print("Operação: Ler ficheiro")
            print('-'*30)
            lista=lerficheiro(input('Ficheiro? '))
        elif op == "3":
            print("Operação: Listar clientes")
            print('-'*30)
            print(listarclientes('chamadas1.txt'))
        elif op == "4":
            print("Operação: Fatura")
            fatura()
        else:
            print('Introduzir uma operação válida!')
            

main()
