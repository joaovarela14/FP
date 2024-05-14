# On a chessboard, positions are marked with letters between a and h for the column and a
# number between 1 and 8 for the row. The first place on the board, a1, is black. The next
# is white, alternating across a row. Odd rows start with black, even rows start with white.

# Give a 2 character input string with a letter (a-h) and a number (1-8), print "Black" or
# "White" indicating if the square is black or white.


inputStr = 'a1' 

letras = ['a','b','c','d','e','f','g','h']

letraspares=[]

letrasimpares=[]

pares=[2,4,6,8]

impares=[1,3,5,7]


for i  in range(0,len(letras)):
    if i % 2 == 0:
        letraspares.append(letras[i])
    else:
        letrasimpares.append(letras[i])


numero=int(inputStr[1])
letra=inputStr[0]

if (numero in pares and letra in letraspares) or (numero in impares and letra in letrasimpares):
    print("White") 
else: print("Black") 