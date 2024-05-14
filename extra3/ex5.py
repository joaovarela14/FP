"""A função main define uma lista de tuplos com informação sobre acções de diversas empresas transacionadas em bolsas de várias cidades.
 Cada tuplo contém os campos: empresa, cidade, preço-de-abertura, preço-de-fecho, volume
 Defina uma função printStocks(stocks) para mostrar a tabela com as colunas formatadas como no exemplo abaixo.
  Inclua uma coluna com a valorização da ação em percentagem.
   Por exemplo, se o preço de abertura for 10.00 e o de fecho for 9.50, a valorização será de -5\%. 
   Note que esta função é chamada pela função main e não deve modificar a lista passada no argumento.
 """


def printStocks(stocks):
   listadoaço=[]
   for i in stocks:
      nome = i[0]
      cidade = i[1]
      pa = round(i[2],2)
      pf= round(i[3],2)
      volume = i[4]
      valorizacao = ((pf-pa)/pa)*100
      valorizacao=round(valorizacao,1)
      listadoaço.append([nome,cidade,pa,pf,volume,valorizacao])
      
   for i in listadoaço:
      print(' {:10}{:20}{:>10}{:>10}{:>10}{:>8}%'.format(i[0],i[1],i[2],i[3],i[4],i[5]))