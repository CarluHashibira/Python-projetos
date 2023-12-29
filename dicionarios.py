# Dicionarios

elemento = {
    'z': 3,
    'nome': 'Litio',
    'grupo': 'Metais Alcalinos',
    'densidade': 0.534
}

print(f'Elemento: {elemento['nome']}')
print(f'Densidade: {elemento['densidade']}')
print(f'O dicionario possui {len(elemento)} elementos.')

# Atualizar uma entrada

elemento['grupo'] = 'Alcalinos'
print(elemento)

# Adicionar uma entrada

elemento['periodo'] = 1
print(elemento)

# Exclusão de itens em dicionarios

#del elemento['periodo']
#print(elemento)

# Apagar todos os itens

#elemento.clear()
#print(elemento)

print(elemento.items())
for i in elemento.items():
    print(i)

# Mostra apenas as chaves
    
print(elemento.keys())
for i in elemento.keys():
    print(i)

# Mostra apenas os valores
    
print(elemento.values())
for i in elemento.values():
    print(i)