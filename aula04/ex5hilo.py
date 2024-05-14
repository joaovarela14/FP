import random

def main():
    secret = random.randrange(1, 101)
    resposta=1
    tentativa=0
    while resposta != secret:
        resposta=int(input("Número: "))
        assert 0<resposta<100, "Número tem de ser e entre 0 e 100"
        if resposta < secret:
            print("Low")
        else:
            print("High")
        tentativa+=1
    
    print("Acertaste! O número secreto era o", secret)
    print("Utilizaste {} tentativas para adivinhar o número secreto".format(tentativa))




main()

