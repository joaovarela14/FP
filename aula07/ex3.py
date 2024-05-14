def listContacts(dic):
    """Print the contents of the dictionary as a table, one item per row."""
    print("{:>12s} : {}".format("Numero", "Nome"))
    for num in dic:
        print("{:>12s} : {}".format(num, dic[num]))

def filterPartName(contacts, partName):
    for k,v in contacts.items():
        if partName in v:
            print(f"Nome: {v}   Número: {k}")
        

   
def removernumero(contacts, numero):
    if numero in contacts:
        print(f"O número {numero} ({contacts[numero]}), foi eliminado da lista de contactos")
        del contacts[numero]
    else:
        print("Número não resgistado")

def adicionar(contacts):
    nome = input("Nome: ")
    numero=input("Número: ")
    morada=input("Morada: ")
    contacts[numero] = (nome,morada)

def numerosearch(numero,contacts):
    if numero in contacts:
        print(f"O número {numero} corresponde ao contacto: {contacts[numero]}")
    
    else :
        print("Número não resgistado")


def menu():
    
    print()
    print("-"*30)
    print()
    print("(L)istar contactos") 
    print("(A)dicionar contacto")
    print("(R)emover contacto")
    print("Procurar (N)úmero") 
    print("Procurar (P)arte do nome") 
    print("(T)erminar")  
    print()
    op = input("opção? L/A/R/N/P/T ").upper()   
    return op


def main():
    print("Menu de telemóvel")
    

    contactos = {"234370200": ("Universidade de Aveiro","Aveiro"),
        "727392822": ("Cristiano Aveiro","Viseu"),
        "387719992": ("Maria Matos", "Coimbra"),
        "887555987": ("Marta Maia","Aveiro"),
        "876111333": ("Carlos Martins","Penafiel"),
        "433162999": ("Ana Bacalhau","Faro")
        }

    op = ""
    while op != "T":
        op = menu()
        
        if op == "T":
            print("Fim")
        elif op == "L":
            print("Operação: Listar contactos")
            print("Contactos:")
            listContacts(contactos)
        elif op == "P":
            print("Operação: Procurar parte do nome")
            busca=input("Parte do nome: ")
            filterPartName(contactos,busca)
        elif op == "R":
            print("Operação: Remover contacto")
            numero=input("Número que deseja remover: ")
            removernumero(contactos,numero)
        elif op == "A":
            print("Operação: Adicionar contacto")
            adicionar(contactos)
        
        elif op == "N":
            print("Operação: Procurar número")
            numero=input("Número que deseja procurar: ")
            numerosearch(numero,contactos)
            
        else:
            print("Não implementado!")
main()

