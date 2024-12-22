# Exercicio 1
# cpf = input('Digite seu cpf: ')

# cpfformatado = cpf.replace('.','').replace('-','')

# if(len(cpfformatado) == 11 and cpfformatado.isnumeric()):
#     print(cpfformatado)

# # if(cpfformatado.isnumeric and cpfformatado == 11):
# #     print('cpf valido')
# # else:
# #     print('digite somente numeros')


"""
    Exercicio 2
"""

email = input('Digite seu e-mail: ')


if('@' in email and '.com' in email):
    print('E-mail válido')
else:
    print(f'E-maiil invalido {email}')