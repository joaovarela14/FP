def hms2sec(h,m,s):
    segundos=h*3600+m*60+s
    print('{} horas, {} minutos e {} segundos corresponde a {} segundos'.format(h,m,s,segundos))
    return segundos

horas=int(input("Horas: "))
minutos=int(input("Minutos: "))
seg=int(input("Segundos: "))
hms2sec(horas,minutos,seg)