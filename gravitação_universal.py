# Calcular força gravitacional utiulizando a formual de Newton F = G M1M2/d²

# Função para calcular a força gravitacional
def calcular_forca_gravitacional(massa1, massa2, distancia):
    
    G = 6.674 * (10**-11)
    
    # Cálculo da força gravitacional
    forca = G * (massa1 * massa2) / (distancia ** 2)
    
    return forca

massa1 = float(input("Digite a massa do primeiro objeto (em kg): "))
massa2 = float(input("Digite a massa do segundo objeto (em kg): "))
distancia = float(input("Digite a distância entre os objetos (em metros): "))

resultado = calcular_forca_gravitacional(massa1, massa2, distancia)

# resultado
print(f"A força gravitacional entre os objetos é de {resultado:.2e} Newtons.")
