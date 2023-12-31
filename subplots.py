import matplotlib.pyplot as plt

# # Criar uma figura e uma grade de subplots
# fig, axs = plt.subplots(nrows=1, ncols=2)

# # Adicionar dados ao subplot esquerdo
# axs[0].plot([1,2,3,4,5],[1,3,4,2,5], linewidth=2, color='#502299', label='esquerda')
# axs[0].set_title('Subplot do lado esquerdo.')

# # Adicionar dados ao subplot direito
# axs[1].barh(['A', 'B', 'C', 'D'],[8, 15, 6, 7], color='orange')
# axs[1].set_title('Subplot do lado direito.')

# axs[0].legend()

# fig.suptitle('Aula de Subplots com Matplotlib')
# fig.tight_layout(pad=2.0)

# plt.show()

cm = 1/2.54 # conversão de polegada em centimetro
fig, axs = plt.subplots(2, 2, figsize=(25*cm, 25*cm), gridspec_kw={'width_ratios':[1,2]})

# Subplots
# # Adicionar dados ao subplot superior esquerdo
axs[0,0].plot([1,2,3,4,5],[1,3,4,2,5], linewidth=2, color='#502299', label='esquerda')
axs[0,0].set_title('Subplot do lado superior esquerdo.')

# # Adicionar dados ao subplot superior direito
axs[0,1].barh(['A', 'B', 'C', 'D'],[8, 15, 6, 7], color='orange')
axs[0,1].set_title('Subplot do lado superior direito.')

# # Adicionar dados ao subplot inferior esquerdo
axs[1,0].bar(['A', 'B', 'C', 'D'],[8, 15, 6, 7], color='g')
axs[1,0].set_title('Subplot do lado inferior esquerdo.')

# # Adicionar dados ao subplot inferior direito
axs[1,1].pie([30,20,40], labels=['A', 'B', 'C'])
axs[1,1].set_title('Subplot do lado inferior direito.')

fig.suptitle('Aula de Subplots com Matplotlib')
fig.tight_layout(pad=2.0)

plt.show()