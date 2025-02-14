"""
Lista em Python
Tipo list - Mútavel
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e Fatiamento
Métodos Úteis: append, insert, pop, del, clear, extend, +
Create read update delete
criar, ler, alterar, apagar = lista[i] (CRUD)
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
"""
#        0   1   2   3
lista = [10, 20, 30, 40]
lista.append('luiz')
nome = lista.pop()
lista.append(1233)
del lista[0]
#lista.clear() apaga a lista
lista.insert(3, 5 ) # adiciona ao indice da lista. 3 é o indce
print (lista)