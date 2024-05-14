tempo = int(input("Segundos: "))

h = tempo // 3600 

extra = tempo % 3600

m = (extra  // 60)

s = extra % 60

print("{:02d}:{:02d}:{:02d}".format(h, m, s))



