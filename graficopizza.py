import matplotlib.pyplot as plt

linguagens = ['Python', 'JavaScript', 'C#', 'Ruby']
quantidades = [300, 270, 150, 40]
cores = ('#660033', 'blue', 'yellow', 'g')
distancia = (0, 0, 0.2, 0)

plt.pie(quantidades, labels=linguagens, colors=cores, explode=distancia, autopct='%1.1f%%', startangle=90)

plt.title('Preferencias de linguagens de Programação')
plt.legend(title='Linguagens', loc='best', bbox_to_anchor=(1, 0.8))

plt.show()