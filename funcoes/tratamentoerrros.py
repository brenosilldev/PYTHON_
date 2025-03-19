"""
    Tratamento de erros

"""



def verificaremail(email):
    try:
        verificado = email.index('@')
        servidor = email[verificado:]

        if 'gmail' in servidor:
            return  'gmail'
    except:
        print('E-mail não tem @.')

   #  try:
   #      if '@' in email:
   #          return 'Existe'
   # except:
   #      print('erro')


email = input('Digite aqui')
print(verificaremail(email))


