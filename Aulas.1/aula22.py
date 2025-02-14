# Operadores Lógicos
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser verdadeiras.
# Se qualquer valor for considerado falso, a expressão
# inteira será avaliada naquele valor
# São considerados falsy (que vc ja viu)
# 0 0. 0 ' ' False 
# Também existe o tipo None que é usado para representar
# um não valor.

#entrada = input('[E]ntrada [S]ainda:')
#senha_digitada = input('Senha:')

#senha_permitida = '123456'
# if só sera execultado se toda expressaão for True

#if (entrada == 'E' or entrada == 'e' )and senha_digitada == senha_permitida:
    #print('Entrar')
#else:
    #print('Sair')

# Avaliação de curto circuito
   # print (True and True) # retorna True
    
# Avaliação de curto circuito para (or)
senha = input('senha:') or 'sem senha'
print(senha)