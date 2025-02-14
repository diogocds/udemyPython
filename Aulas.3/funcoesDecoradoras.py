# Funções decoradoras e decoradores
# Decorar = Adicionar / Remover / Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções
# Decoradores são usados ​​para fazer o Python
# usar as funções decoradoras em outras funções.
# Decoradores são "Syntax Sugar"


# def cria_funcao(func):
#     def interna(*args, **kwargs):
#         print('Vou te decorar')
#         for arg in args:
#             e_string(arg)
#         resultado = func(*args, **kwargs)
#         print(f'O seu resultado foi {resultado}')
#         print('Ok, você foi decorada')
#         return resultado
#     return interna # Termina a funcao decoradora

# def inverte_string(string):
#     return string[::-1]

# def e_string(param):
#     if not isinstance(param, str):
#         raise TypeError('param deve ser uma str')
# inverte_string_checando_parametro = cria_funcao(inverte_string)
# invertida = inverte_string_checando_parametro('123')
# print(invertida)

# Decoradores (Syntax Sugar)

def cria_funcao(func):
    def interna(*args, **kwargs):
        print('Vou te decorar')
        for arg in args:
            e_string(arg)
        resultado = func(*args, **kwargs)
        print(f'O seu resultado foi {resultado}')
        print('Ok, você foi decorada')
        return resultado
    return interna # Termina a funcao decoradora

@cria_funcao # Syntax Sugar ( @ ) chama função Decoradores (Decoradora)
def inverte_string(string):
    return string[::-1]

def e_string(param):
    if not isinstance(param, str):
        raise TypeError('param deve ser uma str')

invertida = inverte_string('123')
print(invertida)