import math

from math import cos, sqrt , acos, degrees

cata = float(input("Medida do cateto A: "))

catb = float(input("Medida do cateto B: "))

hipo = sqrt(cata**2 + catb**2)

print("Hipotenusa= ",hipo)

cos = cata/hipo

ang=degrees(acos(cos))

print("O angulo entre o cateto A \n e a hipotenusa é igual a {:.2f}".format(ang))
