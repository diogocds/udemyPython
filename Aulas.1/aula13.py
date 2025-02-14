nome = 'Diogo Cunha'

altura = 1.89

peso = 89

imc = peso / altura ** 2


# imc... # IMC = peso / (altura x altura)
# Diogo cunha tem 1.89 de altura,
# pesa 85 quilos e seu IMC é
                                # 2f refere se a quantidades de casas decimais que queremos imprimir no resultado.
linha_1 = f'Nome: {nome} tem {altura:,.2f} de altura' # Ex: 1
linha_2 = f'Nome: {nome} tem {altura:,.1f} de altura' # Ex: 2
linha_3 = f'pesa {peso} quilos e seu imc é'
Linha_4 = f'{imc:.2f}'


print(linha_1)
print(linha_2)
print(linha_3)
print(Linha_4)
