"""
    lIST COMPREHESION
"""
from traceback import print_tb
from typing import Any

# preco = [1,2,3,4,5,6,7,8,9]
#
# contagem = [precos * 0.7 > 2  for precos in preco ]
# print(contagem)

# valor = [ 1500,150,2100,1950]
# produto = ['vinho','cafeita','tv','iphone']
# listaaux = list(zip(produto,valor))
# listaaux.sort(reverse=True)
# print(listaaux)
# novalista = [produto for produto,valor in listaaux]
# print(novalista)


# IF

# meta = 1000
# vendas_produtos = [1500, 150, 2100, 1950]
# produtos = ['vinho', 'cafeiteira', 'microondas', 'iphone']
#
#
# novalista = [produto for i,produto in enumerate(produtos) if vendas_produtos[i] >= meta]
# print(novalista)

vendas_produtos = [1500, 150, 2100, 1950]
novalista = [valor if valor > 500 else 'Teste' for valor in vendas_produtos]
print(novalista)
