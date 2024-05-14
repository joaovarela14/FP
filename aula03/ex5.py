from tkinter import Y
from unicodedata import mirrored


def max2(a,b):
    if a>b:
        #print("O maior número é o",a)
        maior=a
    else:
        #print("O maior número é o",b)
        maior=b
    return maior

print("Insere 3 valores inteiros, irei te dizer qual deles é maior :)")
x=int(input("Primeiro número: "))
y=int(input("Segundo número: "))
z=int(input("Terceiro número: "))
max2(x,y)

def max3(a,b,c):
    maior2=max2(a,b)
    maior2=max2(maior2,c)
    print("O maior número é o ",maior2)

max3(x,y,z)

