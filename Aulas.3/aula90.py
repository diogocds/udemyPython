# empacotamentos e desempacotamento de dicionários


a, b = 1, 2
a, b, = b, a
# print(a, b)

# pessoa = {
#     'nome': 'Aline',
#     'sobrenome': 'Souza',


# (a1, a2), (b1, b2) = pessoa.items()
# print(a1, a2)
# print(b1, b2)

# for chave, valor in pessoa.item():
#     print(chave, valor)
pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}

dados_pessoa ={
    'idade': 16,
    'altura': 1.6,
}

pessoas_completa = {**pessoa, **dados_pessoa}
# print(pessoa, dados_pessoa)

# args e kwargs
# args ( Já vimos)
# kwargs - keyword arguments(argamentos nomeados)
def mostro_argumentos_nomeados(*args, **kwargs):
    for chave, valor in kwargs.items():
        print(chave, valor)


mostro_argumentos_nomeados(nome='Joana', qlq=123)

