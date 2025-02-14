"""
Exercício
Peça ao usuario para digitar seu nome
Peça ao usuário para digitar sua idade 
Se o nome e idade forem digitados:
    Exiba:
        seu nome é 
        nome invertido é
        Seu nome contém Espaços
        Seu nome tem (qtd) letras
        A ultima letra do seu nom e é 
Se nada fpor digitado em nome ou idade:
    Exiba "Descupe, você deixou campos vazios.
"""
"""
Jeito que fiz uma parte

nome = 'Diogo cunha'
idade = 37
print ('Seu Nome é:', nome)
print('Nome invertido é:', nome[::-1])
print('Seu nome tem quantas letras?', len(nome))
print(' A ultima letra do seu nome é?', nome[::-11])
"""
"""
Correção
"""
nome = input('Digite o seu nome: ')
idade = input('Digite sua idade: ')

if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')

    if ' ' in nome:
        print('Seu nome contém espaços')
    else:
        print('Seu nome NÃO contém espaços')

    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é {nome[-1]}')
else:
    print("Desculpe, você deixou campos vazios.")
