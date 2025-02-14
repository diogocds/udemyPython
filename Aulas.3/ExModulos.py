import copy

# copiar, sorted, produtos.sort
# Exercícios

produtos  = [
    { 'nome' : 'Produto 5' , 'preco' : 10.00 },
    { 'nome' : 'Produto 1' , 'preco' : 22.32 },
    { 'nome' : 'Produto 3' , 'preco' : 10.11 },
    { 'nome' : 'Produto 2' , 'preco' : 105.87 },
    { 'nome' : 'Produto 4' , 'preco' : 69.90 },
]

# Aumente os preços dos produtos a seguir em 10%
novos_produtos =[
    {**produtos, 'preco': round(produtos['preco']* 1.1, 2)}
    for produtos in copy.deepcopy(produtos)
]

# print(*produtos, sep='\n')
# print()
# print(*novos_produtos, sep='\n')

# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)
produtos_ordenados_por_nome = sorted(
    copy.deepcopy(produtos),
    key= lambda produtos: produtos['nome'],
    reverse=True
)

# print(*produtos, sep='\n')
# print()
# print(*produtos_ordenados_por_nome, sep='\n')


# Ordene os produtos por preço crescente (do menor para maior)
produtos_ordenados_por_preco = sorted(
    copy.deepcopy(produtos),
    key= lambda produtos: produtos['preco'],
)

# FINAL

print(*produtos, sep='\n')
print()
print(*novos_produtos, sep='\n')
print()
print(*produtos_ordenados_por_nome, sep='\n')
print()
print(*produtos_ordenados_por_preco, sep='\n')