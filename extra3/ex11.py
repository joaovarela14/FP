"""Complete onlyCaps(S) para devolver uma string que contenha apenas as letras maiúsculas da string S. 
Por exemplo, onlyCaps("John Fitzgerald Kennedy") deve devolver "JFK".
 A solução tem de ser recursiva e não pode usar ciclos."""


def onlyCaps(S):
    if len(S) == 0:
        return ""
    elif S[0].isupper():
        return S[0] + onlyCaps(S[1:])
    else:
        return onlyCaps(S[1:])
