"""
For + Range
range -> range(start, stop, step)

iterável -> str, rangr, etc
iterador -> quem sabe entregar um valor por vez
next -> me entrgue o proximo valor 
iter -> me entregue seu iterator
"""

# numeros = range(0, -10, -2)

# for numero in numeros:
#     print(numero)

# texto = iter('Luiz')
# print(next(texto))
# print(next(texto))
# print(next(texto))
# print(next(texto))

texto = 'Luiz'  # iterável
# iteratador = iter(texto) # iterator

# while True:
#     try:
#          letra = next(iteratador)
#          print(letra)
#     except StopIteration:
#          break
for letra in texto: # for resume todo o programa while, try etc. 
    print(letra)


