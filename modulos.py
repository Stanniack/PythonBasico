# agora, com math. eu uso as funções matemáticas
import math
import random
#biblioteca random
n = random.randint(1, 10)
print(n)

import emoji
print(emoji.emojize('Teste emoji: :earth_americas:', use_aliases=True))


#Sorteando item em uma lista
lista = ['Mateus', 'Ana', 'João', 'Sampaio']
print(random.choice(lista))
# Random dentro de uma lista
random.shuffle(lista)
print(lista)
