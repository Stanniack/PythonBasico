frase = 'Python x Java'

# Troca os índices da string, se existir
print(frase.replace('Python', 'JavaScript'))

print(frase.upper())
print(frase.lower())

# Tira espaços do começo e fim da string
frase3 = '         Teste    '.strip()
print(frase3)

# Une caracter na string
frase4 = 'Teste de string '
print('_'.join(frase4))

# Divide a string por palavra/espaço
print(frase4.split())

# Escrever texto grande sem quebra de linha
print("""Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. """)

# Conta a quantidade do caracter informado na string
frase5 = 'Mateus Vitor Celestino'
print(frase5.count('e'))

# tamanho da var
print(len(frase5))



