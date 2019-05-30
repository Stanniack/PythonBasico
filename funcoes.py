def mandamsg(msg):
    print(msg)


mandamsg('Oláááá')


def calcula(num1, num2):
    # Exemplo de importação local
    import datetime
    """

    :param num1: Primeiro número para somar
    :param num2: Segundo número para somar
    :return: Retorna num1+ num2
    """
    return num1 + num2


mandamsg(calcula(5, 5))


# Empacotamento de parâmetros
def printanumeros(*num):
    soma = 0
    print(num)
    for n in num:
        soma += n

    print(f'Soma dos valores empacotados: {soma}')


printanumeros(1, 5)
printanumeros(7, 8, 10, 14)
printanumeros(1)


# Docsstrings
help(calcula)


# Parâmetro opcional
def calcula2(num1, num2, num3=0):
    return num1 + num2 + num3


# Não informei o terceiro parâmetro
n = calcula2(5, 3)
# Usar variáveis globais dentro de funções locais
global a


