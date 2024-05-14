from cgi import print_arguments
from xml.sax.handler import property_interning_dict

#𝑝(0), 𝑝(1), 𝑝(2) e 𝑝(𝑝(1)).

def polinomio(x):
    p=x**2+2*x+3
    return p

def f(PX):
    j=PX**2+2*PX+3
    return j

print("𝑝(0)=",polinomio(0))
print("𝑝(1)=",polinomio(1))
print("𝑝(2)=",polinomio(2))
print("𝑝(p(1))=",f(polinomio(1)))




