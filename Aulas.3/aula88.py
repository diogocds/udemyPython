# Introdução à função lambda (função anônima de uma linha)
# A função lambda é uma função como qualquer
# outra em Python. Porém, são funções anônimas
# que contém apenas uma linha. Ou seja, tudo
# deve ser contido dentro de uma única
# expressão.

# lista = [
#     {'nome' :'Luiz', 'sobrenome':'Miranda'},
#     {'nome' :'Maria', 'sobrenome':'Oliveira'},
#     {'nome' :'Daniel', 'sobrenome':'Silva'},
#     {'nome' :'eduardo', 'sobrenome':'Moreira'},
#     {'nome' :'Aline', 'sobrenome':'Souza'},
# ]

# lista = [1, 2, 3, 4, 5, 6, 6 , 21,]
# lista.sort(reverse=True)
# # sorted(lista)

lista = [
    {'nome' :'Luiz', 'sobrenome':'Miranda'},
    {'nome' :'Maria', 'sobrenome':'Oliveira'},
    {'nome' :'Daniel', 'sobrenome':'Silva'},
    {'nome' :'Eduardo', 'sobrenome':'Moreira'},
    {'nome' :'Aline', 'sobrenome':'Souza'},
]

# def orderna(item):
#     return item['sobrenome']

# lista.sort(key=lambda item: item['nome'])

def exibir(lista):
    for intem in lista:
        print(intem)
    print()

l1= sorted (lista, key=lambda item: item['nome'])
l2= sorted (lista, key=lambda item: item['sobrenome'])

exibir(l1)
exibir(l2)


# for item in lista:
#     print(item)
