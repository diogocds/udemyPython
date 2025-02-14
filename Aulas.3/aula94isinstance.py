# isinstance - para saber se objetos pe de determinado tipo
lista = ['a', 1, 1.1, True, [0, 1, 2], (1, 2),
{0, 1}, {'nome': 'luiz'}
]

for item in lista:
    if isinstance(item, set):
        print('set')
        item.add(5)
        print( item, isinstance(item, set))

    elif isinstance(item, str):
        print('str')
        print(item.upper())

    elif isinstance(item, (int, float)):
        print('num')
        print(item, item * 2)
else:
       print('outros')
       print('item')

