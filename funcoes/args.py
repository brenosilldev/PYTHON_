"""

    Multiplos argumentos em um função
"""
# Se torna uma tupla -
# def min(*numeros):
#     soma = 0
#     for a in numeros:
#         soma += a
#
#     return  soma
#
# print(min(10,20,3,6,70,9,3,1,3,4,3,0))
#

# Varios argumentos podem ser passados - formato de dicionario
# def min(preco,**adicionais):
#     print(adicionais)
#     if 'desconto' in adicionais:
#         preco *= (1-adicionais['desconto'])
#     if 'garantia_extra' in adicionais:
#         preco += adicionais['garantia_extra']
#     if 'imposto' in adicionais:
#         preco *= (1 + adicionais['impostos'])
#     return  preco
#
#
# print(min(1000,desconto=0.3,garantia_extra=200,impostos=0.7))

# Ordem dos argumentos

#
# def functeste(arg1,ar2,*numeros,**numerosargas):
#     print(arg1)
#     print(ar2)
#     print(numeros)
#     print(numerosargas)
#
#
#
# print(functeste(10,20,30,30,30,30,30,40,474580,51001421120,teste=1,teste2=2,teaste='ebvfue'))