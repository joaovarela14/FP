x1 = float(input("x1? "))
x2 = float(input("x2? "))
x3 = float(input("x3? "))

if x1>x2 and x1>x3:
    print("O maior número apresentado é o ",x1)
elif x3>x1 and x3>x2:
    print("O maior número apresentado é o ",x3)
else:
    print("O maior número apresentado é o ",x2)