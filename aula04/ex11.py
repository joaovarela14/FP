numero=int(input("Número: "))
assert numero > 0, "Insira um número positivo"
soma=0
categoria="none"
print("Lista dos divisores de ",numero) 
for i in range(1,numero):
    if numero%i==0:
        print (i)
        soma+=i
    
if soma < numero:
    categoria="Deficiente"
elif soma == numero:
    categoria="Perfeito"
else:
    categoria="Abundante"

print("O número {} insere-se na categoria: '{}', visto que a soma dos seus dividores é igual a {}.".format(numero,categoria,soma))