# Given a string s, return the longest prefix that is repeated somewhere else in the string. 
# For example, "abcdabejf" would return "ab" as "ab" starts at the beginning of the string
# and is repeated again later. Do not use the find method.

def longestPrefixRepeated(s):
    resposta = ""
    for i in range (1,len(s)):
        if s[:i] in s[i:]:
            resposta=s[:i] 
    
    return resposta


    