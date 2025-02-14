# frase = 'O Python é uma linguagem de programação '\
# 'multiparadigma.'\
# 'Python foi criado por Guido van Rossum.'#.upper() ponto upper Deixa a frase coom letras maisculas.

# print(frase)
# print(frase.count('Python'))
frase = 'aaaooo'

i = 0 
while i < len(frase):
    letra_atual = frase[i]
    quantas_vezes_letra_apareceu = frase.count(letra_atual)
   
    print(letra_atual, quantas_vezes_letra_apareceu)
    i += 1