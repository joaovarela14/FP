"""O código abaixo lida com comboios de mercadorias. Cada comboio é representado por uma lista de vagões e cada vagão é uma lista com o tipo e a quantidade de mercadoria que transporta. Por exemplo,

t = [['coal', 30], ['rice', 50], ['iron', 5], ['rice', 42], ['coal', 45]]
representa um comboio com 5 vagões: o primeiro vagão tem 30 toneladas de carvão, o segundo tem 50 toneladas de arroz, etc.

A função principal define um dicionário trains que associa nomes a comboios.
 Complete a função trainsPerMerchandise(trains) para criar um dicionário que a cada tipo de mercadoria associe o conjunto dos nomes dos comboios que a transportam."""


def trainsPerMerchandise(trains):
    resposta={}
    for k,v in trains.items():
      for i in v:
         
         if i[0] not in resposta:
            resposta[i[0]]={k}
         else:
            resposta[i[0]].add(k)
            
    return resposta
   