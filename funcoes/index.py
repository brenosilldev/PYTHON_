
# """
# FUNC
# """
# # def Func():
# #     print('Ola')


# # Func()

# def ehalcoolico(bebida,cod_produto):
#     bebida = bebida.upper()
#     if cod_produto in bebida:
#         return True


# produtos = ['CAR46275','TFA23962','TFA64715','TFA69555','TFA56743','BSA45510','TFA44968','CAR75448','CAR23596','CAR13490','BEB21365','BEB31623','BSA62419','BEB73344','TFA20079','BEB80694','BSA11769','BEB19495','TFA14792','TFA78043','BSA33484','BEB97471','BEB62362','TFA27311','TFA17715','BEB85146','BEB48898','BEB79496','CAR38417','TFA19947','TFA58799','CAR94811','BSA59251','BEB15385','BEB24213','BEB56262','BSA96915','CAR53454','BEB75073']

# for produto in produtos:
#     if ehalcoolico(produto,'BEB'):
#         print('Enviar {} para setor de bebidas alcóolicas'.format(produto))
#     elif ehalcoolico(produto,'BSA'):
#         print('Enviar {} para setor de bebidas NÃO alcóolicas'.format(produto))


# print(produto,sep='\n')


def operacoesbasica(num1,num2):
    soma = num1 + num2
    menos = num1 - num2
    mult = num1  * num2
    divisao = num1 / num2
    return (soma,menos,mult,divisao)


print(operacoesbasica(10,2))