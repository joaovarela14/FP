def tax(r):
    if r<=1000:
        funcao=0.1*r
    elif 1000<r<=2000:
        funcao=0.2*r-100
    else:
        funcao=0.3*r-300

    print(funcao)
    return funcao

x=float(input("Insere o valor que desejas calcular: "))
tax(x)

