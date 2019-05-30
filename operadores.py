# Exponenciação - pow(b, e) também serve
print(5 ** 2)
# Divisão inteira
print(5 // 2)

# operadores com string

print('-' * 5)
nome = 'Mateus'
#começa em 20 espaços
print('{:>20}'.format(nome))

#Centralizando em 20 espaços
print('{:^20}'.format(nome))

#Centralizando em 20 espaços com preenchimento qualquer, no caso '='
print('{:=^20}'.format(nome))

#Formatação estilo C
n1 = 1.34
n2 = 2.70
print('{:.3f}'.format(n1/n2))


for i in range(1, 11):
    print('Tabuada do 7: 7x{}: {}'.format(i, 7*i))

for i in ['Java', 'C', 'Python', 'JavaScript']:
    print('Linguagem: {}'.format(i))

for i in range(1, 10, 2):
    print('Incrementando de 2 em 2: {}'.format(i))

