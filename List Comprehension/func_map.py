"""
    MAP - PERCORRE CADA ITEM
    sort ou sorted
"""
#
# produtos = ['ABC ','abc37','eneimMOP','ijde ']
#
#
#
# def Padronizartext(texto):
#     texto = texto.lower()
#     texto = texto.strip()
#     texto = texto.replace(" ","")
#     return texto
#
# produto = list(map(Padronizartext,produtos))
# produtos.sort(key='',reverse=true)
# print(produto)


# Lambda Expressions - Função anonima

#
# funcao = lambda num: (num * 2) - 1
# print(funcao(3))
#
# imposto = lambda preco : preco * (1 + 0.9)
# print(imposto(20))

preco_tecnologia = {'notebook asus': 2450, 'iphone': 4500, 'samsung galaxy': 3000, 'tv samsung': 1000, 'ps5': 3000, 'tablet': 1000, 'notebook dell': 3000, 'ipad': 3000, 'tv philco': 800, 'notebook hp': 1700}


# def calcularpreco (preco):
#     return  preco * 1.3
#
# novopreco = list(map(calcularpreco,preco_tecnologia.values()))
# print(novopreco)

novofilter = dict(list(filter(lambda valor : valor[1] >= 2000,preco_tecnologia.items())))
print(novofilter)