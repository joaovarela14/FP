"""Neste programa, stocks é uma lista de tuplos com informação sobre acções de diversas empresas transacionadas em bolsas de várias cidades.
 Cada tuplo contém os campos: empresa, cidade, preço-de-abertura, preço-de-fecho, volume. A variável stocks2 contém outra lista do mesmo tipo.

Complete a função companyVolume(stocks, city) para devolver uma lista com as empresas e volumes das ações da bolsa da cidade dada.
 Pressione Codecheck para conferir o resultado esperado."""



def companyVolume(stocks, city):
    lista=[]
    for i in stocks:
      if i[1] == city:
         lista.append((i[0],i[-1]))
    return lista