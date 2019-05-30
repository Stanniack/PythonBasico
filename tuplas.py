lista = []
tupla = ()
dicionario = {}

lista.append('Mateus')
print(lista)
print(max(lista))


numeroExtenso = ('Um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
                 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')


while True:
    n = int(input('Digite um número de 0 a 20: '))

    if n >= 0 and n <= 20:
        print(f'Seu número ({n}) por extenso é {numeroExtenso[n - 1]}')
        break;
    else:
        print('Número inválido')

print(max(numeroExtenso))
print(numeroExtenso.count('dois'))


palavras = ('João', 'Mateus', 'Anderson', 'Lucas', 'Maria', 'Fernando')

for each in palavras:
    print(f'\nNa palavra {each} temos as vogais ', end='')
    for letra in each:
        if letra.lower() in 'aàáãâeéêiíîoóôõuúû':
            print(letra.lower(), '', end='')