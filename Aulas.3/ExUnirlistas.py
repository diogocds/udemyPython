# Exercício - Unir listas
# Crie uma função de zíper (como o zíper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Exemplo:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

# Ex1
# def zipper(l1, l2):
#     intervalo = min(len(l1), len(l2))
#     return[
#         (l1[i], l2[i]) for i in range(intervalo)
#     ]

# l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
# l2 = ['BA', 'SP', 'MG', 'RJ']
# print(zipper(l1, l2))

# Ex2 - usa o valores da lista menor (Funcoes do Python)
from itertools import zip_longest #Execulta a lista maior

l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
l2 = ['BA', 'SP', 'MG', 'RJ']
print(list(zip(l1, l2)))
print(list(zip_longest(l1, l2, fillvalue='Rio de Janeiro')))