# Exercicios
# Crie funções que duplicam, triplica e quadriplicam
# o número recebido como parâmetro.


# Minha resoluçaõ: 

def duplicar(numero):
    return numero * 2
print(duplicar(2))


# Correção do exercicio

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador 
    return multiplicar

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(2))
print(triplicar(2))
print(quadruplicar(2))