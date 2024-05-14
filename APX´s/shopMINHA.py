def loadDataBase(fname, produtos):
    with open (fname) as ficheiro:
        ficheiro.readline()
        for linha in ficheiro:
            linha = linha.split(";")
            linha[4] = linha[4].strip("%\n")
            produtos[linha[0]] = (linha[1], linha[2], float(linha[3]) , float(linha[4]) * 0.01)
    
    return produtos


def registaCompra(produtos):
    resposta = None
    registo = {}
    while True:
        resposta = input("Code? ")
        
        if resposta != "":
            resposta = resposta.split()
            codigo = resposta[0]
            
            if codigo in produtos:
                if len(resposta) == 1 or int(resposta[1])<=0:
                        quantidade = 1
                else: quantidade = int(resposta[1])

                    
                nome = produtos[codigo][0] 
                #obtém o nome do produto correspondente ao código introduzido 
                
                preço = (produtos[codigo][2] + produtos[codigo][2] * produtos[codigo][3]) * quantidade  
                #(preço base + iva) x quantidade produtos

                print("{}  {}  {}".format(nome, quantidade, round(preço,2)))

                
                if registo.get(codigo) == None:
                    registo[codigo] = quantidade
                
                else: 
                     registo[codigo] += quantidade

            else: continue
        
        else: break
    
    return registo



def fatura(produtos, compra):
    totaliva = 0
    precobruto = 0
    seccoes = {}

    for codigo_produto in compra.keys():
        produto=produtos[codigo_produto]    #vai buscar o produto correspondente ao código (k)
        seccao_do_produto=produto[1]     #vai buscar o nome da secção corresponde a este produto
 
        seccoes[seccao_do_produto] = seccoes.get(seccao_do_produto,list())    #verifica se já existe uma lista para esta secção no dicionário seccções
        seccoes[seccao_do_produto].append(codigo_produto)     #adiciona  o código (k) do produto à lista correspondente


    for secção in seccoes:
        print(secção)
        for index in range(len(seccoes[secção])):
            codigo  = seccoes[secção][index]      #buscar o código correspondente ao produto pertencente a esta seccção 
            quantidade = compra[codigo]   

            iva = produtos[codigo][2] * produtos[codigo][3] * quantidade    #calcula o iva 
            preco = produtos[codigo][2] * quantidade   #calcula o preço (sem IVA)

            precobruto += preco    #soma todos os preços (sem IVA)
            totaliva += iva     #soma todos os IVA´s
            
            print(f"{compra[codigo] :>4} {produtos[codigo][0] :<30} {'('}{int(produtos[codigo][3]*100):>2}{'%)'} {round((preco+iva),2) :>10}")
            

    
    print(f"{'Total Bruto:' :>41} {round(precobruto,2) :>10}")
    print(f"{'Total IVA:' :>41} {round(totaliva,2) :>10}")
    print(f"{'Total Liquido:' :>41} {round(precobruto+totaliva,2) :>10}")
        


def main(args):
    produtos = {'p1': ('Ketchup.', 'Mercearia Salgado', 1.59, 0.23)}

    loadDataBase("produtos.txt", produtos)
    loadDataBase("produtos1.txt", produtos)

    for arg in args:
        loadDataBase(arg, produtos)
    
    
    MENU = "(C)ompra (F)atura (S)air ? "

    listacompras = []
    while True:
        op = input(MENU).upper()
        
        if op == "C":
            compra = registaCompra(produtos) 
            listacompras.append(compra)

        elif op == "S":
            break
        
        elif op == "F":
            numero = int(input("Numero compra? "))
            while numero <=0 or numero > len(listacompras):      #verifica se o número de compra existe ou se é negativo
                numero = int(input("Numero compra? "))
            
            fatura(produtos,listacompras[numero-1])

    print("Obrigado!")


import sys
if __name__ == "__main__":
    main(sys.argv[1:])

