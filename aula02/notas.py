#CALCULADORA DE NOTAS

ctp=float(input("Nota de CTP: "))
cp=float(input("Nota de CP: "))
NR=cp*0.70+ctp*0.30
if ctp<65 or cp<65:
    print("A nota final é igual a 66 ")
    atpr=float(input("Nota do teste teórico-prático(ATPR): "))
    apr=float(input("Nota do teste prático(APR): "))
    notafinal=  max(ctp,atpr)*0.30+max(cp,apr)*0.70
    if notafinal<10:
        print("A nota final é igual a {:.2f} valores. O aluno foi reprovado!".format(notafinal))
    else:    
        print("A nota final é igual a {:.2f} valores. O aluno foi aprovado!".format(notafinal))
   
elif NR<100:
    atpr=float(input("Nota do teste teórico-prático(ATPR): "))
    apr=float(input("Nota do teste prático(APR): "))
    notafinal=  max(ctp,atpr)*0.30+max(cp,apr)*0.70
    print("A nota final é igual a {:.2f} valores. O aluno foi reprovado!".format(notafinal))
else: 
    print("A nota final é igual a {:.2f} valores. O aluno foi aprovado!".format(NR))

