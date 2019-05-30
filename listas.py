lista = [10,7,5,11,5,7,8]

# Apenas adicione no final
lista.append(6)
# Adiciona na posição 4 o número 16
lista.insert(4, 16)
# Funciona como uma pilha, mas dá para dizer o índice a ser removido
lista.pop(3)

# Forma de popular uma lista com range
listaRange = list(range(1, 11))

print(lista)
print(listaRange)

# Sort na lista, e sort reverso
print(lista.sort())
print(lista.sort(reverse=True))

a = [1, 2, 3]
b = [4, 5, 6]

# Ligação de listas, se alterar uma, a outra também será alterada - ISSO NÃO É ATRIBUIÇÃO
a = b
print(a)
# Isso é uma atribuição de lista
a = b[:]
print(a)

if lista.__contains__(10):
    print('Contém 10')
else:
    print('Não contém 10')




pilha = []

while True:
    eq = str(input('Digite a equação: ')).strip()

    for digito in eq:

        if '(' in digito:
            pilha.append(digito)
        elif ')' in digito:
            if len(pilha) == 0:
                pilha.append(digito)
                break
            else:
                pilha.pop()

    if len(pilha) == 0:
        print('Equação correta.')
    else:
        print('Equação incorreta.')

    pilha = []

    n = input('Deseja continuar S/N: ')

    if n in 'Nn':
        break;


