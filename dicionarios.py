'''
filme = {}
filmes = []

for i in range(0, 3):
     filme['Filme'] = input('Digite o filme: ')
     filme['Ano'] = input('Digite o ano: ')
     filme['Diretor'] = input('Digite o diretor: ')
     filmes.append(filme.copy())


# Pega a chave e os valor
for k, v in filme.items():
    print(f'O {k} é {v}')


# Apenas os valores
for v in filme.values():
    print(f'{v}')


# Apenas as chaves
for k in filme.keys():
    print(f'{k}')

# Mostrando todos os filmes
for filme in filmes:
    print(filme)
'''
'''
for filme in filmes:
    for k, v in filme.items():
        print(f'O {k} é {v}')
'''

# Usando sort no dicionário
import operator
dicionario = {'Mateus': 22, 'João': 24, 'Breno': 20, 'Lucas': 25, 'Anderson': 21}

# Reverse para sort invertido
dicionarioSorted = sorted(dicionario.items(), key=operator.itemgetter(1), reverse=True)

print(dicionarioSorted)

