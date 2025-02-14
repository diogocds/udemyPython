# map, partial, GeneratorType e esgotamento de Iterators

from  functools  import  partial
from  types  import  GeneratorType


# map - para mapear dados
def  print_iter ( iterador ):
    print ( * list ( iterador ), sep = ' \n ' )
    print ()


produtos  = [
    { 'nome' : 'Produto 5' , 'preço' : 10.00 },
    { 'nome' : 'Produto 1' , 'preço' : 22.32 },
    { 'nome' : 'Produto 3' , 'preço' : 10.11 },
    { 'nome' : 'Produto 2' , 'preço' : 105.87 },
    { 'nome' : 'Produto 4' , 'preço' : 69.90 },
]


def  aumentar_porcentagem ( valor , porcentagem ):
    return round ( valor  *  porcentagem , 2 )


aumentar_dez_porcento  =  partial (
    aumentar_porcentagem ,
    porcentagem = 1.1
)

# novos_produtos = [
# {**p,
# 'preco': aumentar_dez_porcento(p['preco'])}
# para p em produtos
# ]


def  muda_preco_de_produtos ( produto ):
    return {
        ** produto ,
        'preço' : aumentar_dez_porcento (
            produto [ 'preço' ]
        )
    }


novos_produtos  =  list ( map (
    muda_preco_de_produtos ,
    produtos
))


print_iter ( produtos )
print_iter ( novos_produtos )

print (
    list ( map (
        lambda  x : x  *  3 ,
        [ 1 , 2 , 3 , 4 ]
    ))
)