# São imutaveis

halogenios = ('F', 'Cl', 'Br', 'I', 'At')
gases_nobres = ('He', 'Ne', 'Ar', 'Xe', 'Kr', 'Rn')
elementos = halogenios + gases_nobres
t1 = (5,2,6,8,7,5,4,5,1,2,6,4,5,5,4,5,9)
print(halogenios)
print(t1.count(3))
print('Fe' in halogenios) # pergunta

# Operações não disponiveis em tuplas: .sort(), .append(), .reverse(), .pop()....

# for elemento in elementos:
#     print(f'Elemento quimico: {elemento}')

# grupo17 = list(halogenios)
# print(grupo17)

grupo1 = ['Li', 'Ha', 'K', 'Rb', 'Cs', 'Fr']
alcalinos = tuple(grupo1)
print(alcalinos)