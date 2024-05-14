seg=int(input("Qual foi a duração da chamada em segundos?"))

if seg <= 60:
    print("O custo da chamada foi de 0,12€")
else:
    custo=((seg)/60)*0.12 
    print("O custo da chamada foi de {:.2f} €".format(custo))
    