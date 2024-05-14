# Este programa demonstra a leitura e utilização de dados de um ficheiro JSON
# com mensagens do Twitter.
# Modifique-o para resolver o problema proposto.


# O módulo json permite descodificar ficheiros no formato JSON.
# São ficheiros de texto que armazenam objetos compostos que podem incluir
# números, strings, listas e/ou dicionários.
import json

# Abre o ficheiro e descodifica-o criando o objeto twits.
with open("twitter.json", encoding="utf8") as f:
    twits = json.load(f)


palavras=list()
for i in twits:
    for j in i["text"].split():
        palavras.append(j)

#palavras=sorted(palavras, key=lambda x: palavras.count(x))
words = {}

#print(palavras)

for i in twits:
    for j in i["text"].split():
        words[j]=palavras.count(j)
        #words[j]=words.get(j,0)+1

words=dict(sorted(words.items(), key=lambda x: words[x]))
print(words)
palavrasordenadas = []
for i in (sorted(words.items(), key=lambda x: words[x])):
    ...
    #print(i, words[i])


        



