palavra= str(input("Palavra: "))

def ispalindrome(s):
    soma=0
    for i in range (len(s)-1):
        if s[i] == s [-(i+1)]:
            soma+=1

    return soma == len(s)-1

print(ispalindrome(palavra))
