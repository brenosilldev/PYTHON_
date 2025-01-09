"""
    FOR E WHILE - ESTRUTURA DE REPETICAO 
"""

# vendas = [1200,300,800,1500,19000,2750,400,300,9000,2500,3000,981,255,300,9000]

# metas = 1000
# qtd = 0
# for i in vendas:
#     if i >= metas:
#         print(f'Valor venda  R${i:,}')
#         qtd +=1

# qtd_func = len(vendas)

# print('O percentual {:.0%}'.format(qtd / qtd_func))


# # ENUMARETE - para pegar o indice do array

# estoque = [1200, 300, 800, 1500, 1900, 2750, 400, 20, 23, 70, 90, 80, 1100, 999, 900, 880, 870, 50, 1111, 120, 300, 450, 800]
# produtos = ['coca', 'pepsi', 'guarana', 'skol', 'brahma', 'agua', 'del valle', 'dolly', 'red bull', 'cachaça', 'vinho tinto', 'vodka', 'vinho branco', 'tequila', 'champagne', 'gin', 'guaracamp', 'matte', 'leite de castanha', 'leite', 'jurupinga', 'sprite', 'fanta']
# nivel_minimo = 50

# for index,item in enumerate(estoque):
#     if item < nivel_minimo:
#         print(f'Precisa comprar mais produtos de {produtos[index]},tem apenas {item} unidades')



# estoque = [
#     [294, 125, 269, 208, 783, 852, 259, 371, 47, 102, 386, 87, 685, 686, 697, 941, 163, 631, 7, 714, 218, 670, 453],
#     [648, 816, 310, 555, 992, 643, 226, 319, 501, 23, 239, 42, 372, 441, 126, 645, 927, 911, 761, 445, 974, 2, 549],
#     [832, 683, 784, 449, 977, 705, 198, 937, 729, 327, 339, 10, 975, 310, 95, 689, 137, 795, 211, 538, 933, 751, 522],
#     [837, 168, 570, 397, 53, 297, 966, 714, 72, 737, 259, 629, 625, 469, 922, 305, 782, 243, 841, 848, 372, 621, 362],
#     [429, 242, 53, 985, 406, 186, 198, 50, 501, 870, 781, 632, 781, 105, 644, 509, 401, 88, 961, 765, 422, 340, 654],
# ]
# fabricas = ['Lira Manufacturing', 'Fábrica Hashtag', 'Python Manufaturas', 'Produções e Cia', 'Manufatura e Cia']
# nivelminimo = 50
# listas = []
# for index,item in enumerate(estoque):
#     for i in item:      
#         if i < nivelminimo:
#             if fabricas[index] in listas:
#                 pass
#             else:
#                 listas.append(fabricas[index])
# print(listas)



i = 0

while(i < 10):
    i += 1
    print(i)


