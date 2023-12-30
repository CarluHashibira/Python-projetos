# Trocar valores entre duas variaveis

var1 = 12
var2 = 31

# var2, var1 = var1, var2
# print(f'Var1: {var1}, var2: {var2}')

# Operador condicional ternário
# menor = var1 if var1 < var2 else var2
# print(f'Menor valor: {menor}')


# Generators

# valores = [1,3,5,7,9,11,13,15]
# quadrados = (item**2 for item in valores)
# print(quadrados)
# for valor in quadrados:
#     print(valor)

# Função enumerate()
# bebidas = ['Café', 'Chá', 'Agua', 'Suco', 'Refrigerante']
# for i, item in enumerate(bebidas):
#     print(f'Indice: {i}, item: {item}')

# temperaturas = [-1, 10, 5, -3, 8, 4, -2, -5, 7]
# total = 0

# for i, t in enumerate(temperaturas):
#     if t < 0:
#         print(f'A temperatura em {i} é negativa, com {t} ºc.')


# Gerenciamento de contexto com with

try:
    a = open('arquivo.txt', 'r', encoding='utf-8')
    print(a.read())
except IOError:
    print(f'Não foi possivel abrir o arquivo')
else:
    a.close()

with open('arquivo.txt', 'r', encoding='utf-8') as a:
    for linha in a:
        print(linha, end='')