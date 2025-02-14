# reduce - faz a redução de um iterável em um valor
from  functools  import  reduce

produtos  = [
    { 'nome' : 'Produto 5' , 'preço' : 10 },
    { 'nome' : 'Produto 1' , 'preço' : 22 },
    { 'nome' : 'Produto 3' , 'preço' : 2 },
    { 'nome' : 'Produto 2' , 'preço' : 6 },
    { 'nome' : 'Produto 4' , 'preço' : 4 },
]


# def funcao_do_reduce(acumulador, produto):
# print('acumulador', acumulador)
# print('produto', produto)
# print
()
# return acumulador + produto['preco']


total  =  reduce (
    lambda  ac , p : ac  +  p [ 'preço' ],
    produtos ,
    0
)

print('Total é' , total )


# total = 0
# para p em produtos:
# total += p['preço']

# print
# (total)

# print(sum([p['preco'] para p em produtos]))