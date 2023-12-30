import csv

# with open('elementos.csv', mode='r', encoding='utf-8') as arq:
#     leitor = csv.reader(arq, delimiter=',')
#     cont = 0
#     for linha in leitor:
#         if cont == 0:
#             print(f'Colunas: {' '.join(linha)}\n')
#             cont += 1
#         else:
#             print(f'Elemento {linha[0]} é o {linha[1]}.')
#             cont += 1
#     print(f'Lidas {cont} linhas.')


# simbolos = []
# with open('elementos.csv', mode='r', encoding='utf-8') as arq:
#     leitor = csv.reader(arq, delimiter=',')
#     for indice, linha in enumerate(leitor):
#         if indice == 0:
#             pass
#         else:
#             simbolos.append(linha[2])
#     print(simbolos)

# Adicionar mais conteudo ao arquivo elementos.csv
with open('elementos.csv', mode='a', encoding='utf-8', newline='') as arq:
    escritor = csv.writer(arq, delimiter=',')
    escritor.writerow(['7', 'Nitrogenio','N','15'])
    escritor.writerow(['8', 'Oxigenio','O','16'])
    escritor.writerow(['9', 'Fluor','F','17'])