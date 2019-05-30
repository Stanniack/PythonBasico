lista = ['Mateus', 'João', 'Anderson']

# Primeira forma de for em py
for i in range(0, len(lista)):
    print(lista[i])

# Segunda forma de for em py
for i in lista:
    print(i)

# Segunda forma mas de maneira enumerada
for pos, i in enumerate(lista):
    print(f'{i} na posição {pos}')

r = 1
for i in range (1, 6):
    r = r * i

print(r)

pilha = [1, 5, 7, 10]
print(pilha)
pilha.pop()
print(pilha)
pilha.append(3)
print(pilha)
