#cada andar tem 3m de altura
#cada morador sobe e desce 2 vezes ao dia logo 4 utilizaçoes por morador 
a=int(input("número de andares: "))
m=int(input("Número de moradores: "))

soma=((1+a)/2)*a #soma de uma progressão aritmética 

dia=3*2*2*m*soma
ano=dia*365
kilometros=ano/1000 
horas=ano/3600

print("O elevador  de um prédio com {} andares e {} moradores percorre,por ano,\n{:.2f} kilometros e está em utilização durante {:.2f} horas".format(a,m,kilometros,horas))



