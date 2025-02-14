# try except, else e finally

try:
    print('Abrir o sistema')
    #8/0
except ZeroDivisionError: #tratando o erro pode usar quantas vezes quiser
    print('Dividiu por zero')
else:
    print( 'Não deu erro')
finally:
    print('Fechar o sistema')