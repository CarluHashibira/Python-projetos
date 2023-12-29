# Atribuindo variaveis

nome_usuario = 'carlos'
print(nome_usuario)

media = 0
n1 = n2 = n3 = n4 = 0.0
nome, idade = 'carlos', 21
estado = True

# Função type()

print(type(media))
print(type(n2))
print(type(nome))
print(type(estado))
print(type(1+2j))

# Função isinstance()

a = 10
b = 'Sol'
print(isinstance(a, int)) # true
print(isinstance(b, str)) # true
print(isinstance(a, float)) # false
print(isinstance(a, (int, float))) # true

a = 40
c = 3
r = a * c
print(r)
