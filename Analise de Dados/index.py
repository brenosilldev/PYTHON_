
"""
    pandas

"""
import pandas as pd
vendadf = pd.read_csv('./arquivos/Contoso - Clientes.csv',sep=';')


# Informaçoes da tabela
print(vendadf.info())

#Pega colunas especificar
print(vendadf[['ID Cliente','E-mail','Data de Nascimento']])

# Aula 4
