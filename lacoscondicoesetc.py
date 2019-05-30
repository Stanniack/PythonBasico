# "Operador ternário" do Pytohon é chamado de condição simplificada
n = 10
print('É 10' if n == 10 else 'Não é 10')

# Início de dicionário - tem que ser com chaves
dicionario = {'Chave1':'Valor1', 'Chave2':'Valor2'}
print(dicionario['Chave1'])

# Verificando se é palíndromo
frase = 'A sacada da casa'.lower().strip()
frase = frase.split()
junto = ''.join(frase)
inversa = ''

for i in range(len(junto) - 1, -1, -1):
    inversa += junto[i]

if junto == inversa:
    print('É palíndroma: {} = {}'.format(junto, inversa))
else:
    print('Não é palíndroma.')


for i in range(5, 0, -1):
    print(i)

from time import sleep
for i in range (10, -1, -1):
    print(i, '\n')
    #sleep(1)

# um for diretamente de uma lista
lista = [int(input()) for i in range(0, 5)]

print(max(lista), min(lista))


