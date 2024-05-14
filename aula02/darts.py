import math

print("Insere o valor das coordenadas onde o dardo acertou. Coloca os valores em milimetros.")
x=float(input("X: "))  #Pedido das variáveis; consideremos o centro do referencial o centro do alvo
y=float(input("Y: "))

dcentro= math.sqrt(x**2+y**2) #Distancia ao centro
if x==0 and y==0:
    pontos=50
else:
    angulo=math.degrees(math.acos(abs(x)/dcentro))  #angulo criado pelo dardo -- considerando sempre um angulo no 1ºquadrante
    pontos=0

if 170<=dcentro<=225.5:
    print("O dardo nao acertou dentro da zona de pontos")
elif dcentro>=225.5:
    print("O dardo nao acertou o alvo")
elif x>=0 and y>=0 and dcentro>16:   #1º Quadrante
    if 0<=angulo<9:
        pontos = 6
    elif 9<=angulo<27:
        pontos=13
    elif 27<=angulo<45:
        pontos=4
    elif 45<=angulo<63:
        pontos=18
    elif 63<=angulo<81:
        pontos=1
    elif 81<=angulo<=90:
        pontos=20
elif x<=0 and y>=0 and dcentro>16:   #2º Quadrante
    angulo=180-angulo
    if 90<=angulo<99:
        pontos = 20
    elif 99<=angulo<117:
        pontos=5
    elif 117<=angulo<135:
        pontos=12
    elif 135<=angulo<153:
        pontos=9
    elif 153<=angulo<171:
        pontos=14
    elif 171<=angulo<=180:
        pontos=11
elif x<=0 and y<=0 and dcentro>16:   #3º Quadrante
    angulo=angulo+180
    if 180<=angulo<189:
        pontos = 11
    elif 189<=angulo<207:
        pontos=8
    elif 207<=angulo<225:
        pontos=16
    elif 225<=angulo<243:
        pontos=7
    elif 243<=angulo<261:
        pontos=19
    elif 261<=angulo<=270:
        pontos=3
elif x>=0 and y<=0 and dcentro>16:   #4º Quadrante
    if 0<=angulo<9:
        pontos = 6
    elif 9<=angulo<27:
        pontos=10
    elif 27<=angulo<45:
        pontos=15
    elif 45<=angulo<63:
        pontos=2
    elif 63<=angulo<81:
        pontos=17
    elif 81<=angulo<=90:
        pontos=20
elif 6.35<dcentro<=16:  
    pontos=25
    print("Parabéns, acertaste no Outer Bullseye")
elif 0<=dcentro<=6.35:
    pontos=50  
    print("UAU! Parabéns, acertaste no Inner Bullseye")

if 162<dcentro<170:    #Double Ring
    pontos=pontos*2
    print("Parabéns! Acertaste no Double Ring")
elif 99<dcentro<107:    #Triple Ring
    pontos=pontos*3
    print("UAU! Parabéns! Acertaste no Triple Ring")

print ("Pontos =",pontos)
