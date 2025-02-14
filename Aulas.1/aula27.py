"""
Formatação básica de strings
s - string
d - int
f - float
.<número de digitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - esquerda
< - direita
^ - Centro
Sinal - + ou -
Ex.: 0>-100, .1f
Conversion flags - 1!r !s !a 
"""
variavel = 'ABC'
print(F'{variavel}')
print(F'{variavel: >10}')
print(F'{variavel: >10}.')
print(F'{variavel: ^10}.')
print(f'{1000.4875635256:.1f}')
print(f'O hexadecimal de 1500 é {1500:08x}')


