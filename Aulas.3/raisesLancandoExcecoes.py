# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions
# Raises, lançando exceções (Erros)

# print(123)
# raise ValueError('Deu erro')
# print(456)

# Ex1
# def divide(n, d):
#     try:
#         return n / d
#     except ZeroDivisionError:
#         return n

# print(divide(8,0))

def nao_aceito_zero(d):
    if d == 0:
        raise ZeroDivisionError('Você está tentando dividir por zero')
    return True


def deve_ser_int_ou_float(n):
    tipo_n = type(n)
    if not isinstance(n, (float, int)):
        raise TypeError(
            f'"{n}" deve ser int ou float. '
            f'"{tipo_n.__name__}" enviado.'
        )
    return True


def divide(n, d):
    deve_ser_int_ou_float(n)
    deve_ser_int_ou_float(d)
    nao_aceito_zero(d)
    return n / d


print(divide(8, '0'))