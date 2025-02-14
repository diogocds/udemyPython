# Funções recursivas e recursividade
# - funções que podem ser chamadas de volta
# - úteis p/ divide problemas grandes em partes menores
# Toda função recursiva deve ter:
# - Um problema que pode ser dividido em partes menores
# - Um caso recursivo que resolve o pequeno problema
# - Um caso baseado em recursão
# - fatorial - n! = 5! = 5 * 4 * 3 * 2 * 1 = 120
# https://brasilescola.uol.com.br/matematica/fatorial.htm

#import sys
#sys.setrecursionlimit(1001) altera o limite de execursao
#  do python obs: nao muito recomendado.

# def  recursiva ( inicio = 0 , fim = 4 ):

#     print ( inicio , fim )

#     # Caso base
#     if  inicio  >=  fim :
#         return  fim

#     # Caso recursivo
#     #contar até chegar ao final
#     inicio  +=  1
#     return  recursiva ( inicio , fim )


# print ( recursiva ())

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)
print(factorial(5))
print(factorial(10))
