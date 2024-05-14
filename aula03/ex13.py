def mdc(a,b):
    r=a%b
    if r==0:
        return b
    else:
        c=mdc(b,r)
        return  c

x=int(input("A= "))
y=int(input("B= "))
print ("O maior divisor comum entre {} e {} é {}.".format(x,y,mdc(x,y)))