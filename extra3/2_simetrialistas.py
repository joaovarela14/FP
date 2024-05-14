# Given a sequence lst, return the longest n so that 
# the first n elements equal the last n elements (with no overlapping).

# Dada uma sequência lst, devolva o maior n tal que
# os primeiros n elementos igualam os últimos n elementos (sem sobreposição).


def firstEqualLast(lst):
    if len(lst)%2 == 0:
        esquerda = lst[:int(len(lst)/2)]
        direita = lst[int(len(lst)/2):]
    
    else:
        esquerda = lst[:int(len(lst)//2)]
        direita = lst[int(len(lst)//2)+1:]


    soma = 0
    i= len(esquerda)  
    j=0

    if esquerda == direita:
        return len(esquerda)
    
    else:
        while i > 0:
            if esquerda[:i] == direita[j:]:
                return len(esquerda[:i])
            else:
                j+=1
                i-=1

        return 0

