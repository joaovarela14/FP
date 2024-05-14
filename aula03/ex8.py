def intersects(a1,b1,a2,b2):
    if b1>a2 and a1<a2:
        print("True")
        print("Os intervalos intersetam-se")
    elif b2>a1 and a2<a1:
        print("True")
        print("Os intervalos intersetam-se")
    else: 
        print("False")
        print("Os intervalos não se intersetam")

print("Primeiro intervalo: ")
x1=int(input("a1: "))
x2=int(input("a2: "))

print("Segundo intervalo: ")
y1=int(input("b1: "))
y2=int(input("b2: "))

intersects(x1,x2,y1,y2)
    