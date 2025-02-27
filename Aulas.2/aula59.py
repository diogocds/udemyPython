"""
Imprecisão de ponto flutuante
Double-precision floating-point format IEEE 754
https://en.wikipedia.org/wiki/Double-precision_floating-point_format
https://docs.python.org/pt-br/3/tutorial/floatingpoint.html
"""
import decimal

# Ex 1
# numero_1 = 0.1
# numero_2 = 0.7
# numero_3 = numero_1 + numero_2
# print(numero_3)
# print(f'{numero_3:.2f}')
# print ((round(numero_3, 2)))

# Ex 2
numero_1 = 6
numero_2 = decimal.Decimal ('0.127')
numero_3 = numero_1 + numero_2
print(numero_3)
print(f'{numero_3:.0f}')
print ((round(numero_3, 0)))