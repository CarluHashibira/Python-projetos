import matplotlib.pyplot as plt

# # Temperaturas
# cidade_a = [32, 30, 27, 28, 29, 24]
# cidade_b = [27, 26, 29, 25, 22, 22]
# cidade_c = [17, 19, 15, 20, 25, 26]

# datas = [5, 10, 15, 20, 25, 30]

# # Criar posições distintas para cada cidade
# posicoes_a = list(range(len(datas)))
# posicoes_b = [pos + 0.25 for pos in posicoes_a]
# posicoes_c = [pos + 0.50 for pos in posicoes_a]

# plt.bar(posicoes_a, cidade_a, width=0.25, color='r', label='Cidade A')
# plt.bar(posicoes_b, cidade_b, width=0.25, color='g', label='Cidade B')
# plt.bar(posicoes_c, cidade_c, width=0.25, color='b', label='Cidade C')

# plt.legend()
# plt.xticks(ticks=posicoes_a, labels=datas)

# plt.show()



# Homicidios
cidade_a = [5, 2, 0, 0, 2, 1]
cidade_b = [2, 1, 2, 4, 3, 6]
cidade_c = [8, 5, 2, 0, 2, 6]

datas = [5, 10, 15, 20, 25, 30]

plt.bar(datas, cidade_a, color='r', label='Cidade A')
plt.bar(datas, cidade_b, bottom=cidade_a, color='g', label='Cidade B')
plt.bar(datas, cidade_c, bottom=[a + b for a, b in zip(cidade_a, cidade_b)], color='b', label='Cidade C')

plt.legend()
#plt.xticks(ticks=datas, labels=datas)
plt.xlabel('Datas')
plt.ylabel('Homicidios')
plt.title('Homicidios nas cidades em dias determinados')

plt.show()