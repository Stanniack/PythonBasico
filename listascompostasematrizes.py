'''
pares = []
impares = []
lista = []

for i in range (0, 7):
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

lista.append(sorted(pares[:]))
lista.append(sorted(impares[:]))

print(lista)


from random import randint
from time import sleep
jogos = []

n = int(input('Quantos jogos quer sortear: '))

for i in range(0, n):
    jogo = [randint(0, 60) for j in range(0, 6)]
    jogos.append(sorted(jogo[:]))
    print(f'Jogo {i + 1}: {jogos[i]}')
    sleep(0.3)
'''


pilha = ['Prato1', 'Prato2', 'Prato3', 'Prato4', 'Prato5']
print(pilha)
pilha.pop()
print(pilha)


