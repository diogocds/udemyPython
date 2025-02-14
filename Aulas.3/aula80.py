# Manipulando chaves e valores em dicionários

pessoa = {}

##
##

chave = 'nome'

pessoa [chave] = 'LuSiz Otávio'
pessoa['sobrenome'] = 'miranda'

print(pessoa[chave]) 
pessoa[chave] = 'maria'


del pessoa ['sobrenome']
print(pessoa)