"""

Interando string com while
"""
#nome = 'Luiz Otávio' # Interáveis
#       012345678910
#     #1110987654321
# tamanho_nome = len(nome)
# print(nome)
# print(tamanho_nome)
# print(nome[3])
# print(nome[-11])

# Exércicio print novo_nome com * entre letras
nome = 'Luiz Otávio' # Interáveis

indice = 0
novo_nome =''
while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1
novo_nome +='*' 
print(novo_nome)