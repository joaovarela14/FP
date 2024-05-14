# Given a string s and a string t, return a string in which all the characters 
# of s that occur in t have been replaced by a _ sign. The comparisons are 
# case sensitive.

def replaceCharactersWithUnderscores(s, t):
    resposta=""
    for i in s:
        if i in t:
            resposta+="_"
        else:
            resposta+=i
            
    return resposta