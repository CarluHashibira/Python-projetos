from matplotlib import pyplot as plt

eixo_x_dias = [1,5,10,15,20,25,30]
eixo_y_temp_max = [28,29,25,32,34,36,31]
eixo_y_temp_min = [21,22,17,23,23,24,20]

plt.title('Temperaturas máximas e minimas')
plt.xlabel('Data')
plt.ylabel('Temperatura')

plt.plot(eixo_x_dias, eixo_y_temp_max, label='Temp Máx')
plt.plot(eixo_x_dias, eixo_y_temp_min, label='Temp Min')

plt.legend(loc='best')
plt.grid(True)
#plt.axis([1,31,5,45])
plt.xlim([1,31])
plt.ylim([-5,50])
print(plt.axis())
# #plt.savefig('meu_grafico.png') #salva o grafico nos arquivos

# Plotar grafico de uma função, como f(x) = x³ + 1
# x = range(1,11,1)
# plt.plot(x, [(val**3 + 1) for val in x])

plt.show()
