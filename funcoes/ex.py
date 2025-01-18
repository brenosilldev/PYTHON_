"""
ex  de carga tributaria
"""
def cargatribuataria(preco,custo,lucro):
    imposto = preco - custo -lucro
    carga = imposto / preco
    return f'Carga {carga:.0%}'


retorno = cargatribuataria(5000,1200,3600)
print(retorno)
# Parei na aula 10