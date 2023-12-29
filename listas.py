# Lista: representa uma sequencia de valores na memoria

# Sintaxe: nome_lista = [valores]

# notas = [5,7,8,6,9]
# print(notas)


# n1 = [4,6,7,8,0,3]
# n2 = [1,6,3,0,12,4]
# valores = n1 + n2
# valores[0] = 9
# print(len(valores))
# print(sorted(valores, reverse=True))
# print(sum(valores))
# print(min(valores))
# print(max(valores))


# valores.append(13)
# print(valores)
# valores.pop()
# print(valores)
# valores.pop(3)
# print(valores)
# valores.insert(3,21)
# print(valores)
# print(12 in valores)


# planetas = ['Mercurio', 'Venus', 'Marte', 'Saturno', 'Urano', 'Netuno']
# for planeta in planetas:
#     print(planeta)


bebidas = []

for i in range(5):
    print(f'Digite uma bebida favorita:')
    bebida = input()
    bebidas.append(bebida)

bebidas.sort()

print(f'\nBebidas escolhidas:')
for bebida in bebidas:
    print(bebida)

print(f'Saude!')