# This program reads the coordinates of two points (x1,y1) and (x2,y2).
import math
x1 = float(input("x1? "))
y1 = float(input("y1? "))
x2 = float(input("x2? "))
y2 = float(input("y2? "))

dist= math.sqrt((x2-x1)**2+(y2-y1)**2)

print (dist)
